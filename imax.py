import argparse
import librosa
import numpy as np
import soundfile as sf
import scipy.signal
from pedalboard import (
    Pedalboard, Compressor, NoiseGate, HighShelfFilter,
    PeakFilter, LowShelfFilter
)
# --- 高速化のために追加 ---
from multiprocessing import Pool, cpu_count
import os
from tqdm import tqdm
# pyfarは不要なので削除し、pyratoをimport
import pyrato as ra


# --- 定数 ---
TARGET_SR = 48000
CHANNEL_LAYOUT = {
    'LS': -30, 'CS': 0, 'RS': 30, 'TCS': 0,
    'LSi': -90, 'RSi': 90, 'LR': -135, 'RR': 135,
    'OFL': -45, 'OFR': 45, 'ORL': -135, 'ORR': 135
}
CHANNEL_ORDER = [
    'LS', 'RS', 'CS', 'TCS', 'LSi', 'RSi', 'LR', 'RR',
    'OFL', 'OFR', 'ORL', 'ORR'
]
# --- IRキャッシュのパスを追加 ---
IR_CACHE_PATH = "imax_ir.npy" # 新しいバージョン用のキャッシュファイル名


# --- 変更なしの関数 ---
def load_audio(file_path):
    print(f"Loading audio from: {file_path}")
    try:
        waveform, sr = librosa.load(file_path, sr=TARGET_SR, mono=False)
    except Exception as e:
        print(f"Error loading file: {e}")
        return None
    if waveform.ndim != 2 or waveform.shape[0] != 2:
        print(f"Error: Input file must be stereo. Found {waveform.shape} shape.")
        return None
    print(f"Loaded {waveform.shape[1] / TARGET_SR:.2f} seconds of audio.")
    return waveform

def save_multichannel_wav(file_path, audio_data, sub_bass_channel):
    print(f"Saving 13-channel audio to: {file_path}")
    main_channels = audio_data.T
    sub_channel = sub_bass_channel.reshape(-1, 1)
    final_output = np.hstack((main_channels, sub_channel))
    try:
        sf.write(file_path, final_output, TARGET_SR, subtype='PCM_24')
        print("File saved successfully.")
    except Exception as e:
        print(f"Error saving file: {e}")

def decorrelate(signal, sr, delay_ms, feedback):
    delay_samples = int(sr * delay_ms / 1000)
    b = np.zeros(delay_samples + 1); b[0] = feedback; b[delay_samples] = 1
    a = np.zeros(delay_samples + 1); a[0] = 1; a[delay_samples] = feedback
    return scipy.signal.lfilter(b, a, signal)

def upmix_to_12_channels(stereo_waveform):
    print("Stage 1: Upmixing stereo to 12 channels...")
    left, right = stereo_waveform[0, :], stereo_waveform[1, :]
    num_samples = left.shape[0]
    mid_signal = (left + right) * 0.707
    side_signal = (left - right) * 0.707
    channels = {name: np.zeros(num_samples, dtype=np.float32) for name in CHANNEL_ORDER}
    channels['CS'] = mid_signal; channels['LS'] = left; channels['RS'] = right
    side_delayed_15ms = np.roll(side_signal, int(TARGET_SR * 0.015))
    side_delayed_20ms = np.roll(side_signal, int(TARGET_SR * 0.020))
    channels['LSi'] = side_delayed_15ms; channels['RSi'] = -side_delayed_15ms
    channels['LR'] = side_delayed_20ms; channels['RR'] = -side_delayed_20ms
    decorrelated_1 = decorrelate(side_signal, TARGET_SR, delay_ms=12, feedback=0.65)
    decorrelated_2 = decorrelate(side_signal, TARGET_SR, delay_ms=18, feedback=-0.7)
    decorrelated_3 = decorrelate(side_signal, TARGET_SR, delay_ms=25, feedback=0.55)
    decorrelated_4 = decorrelate(side_signal, TARGET_SR, delay_ms=32, feedback=-0.6)
    channels['TCS'] = (decorrelated_1 + decorrelated_2) * 0.5
    channels['OFL'] = decorrelated_3; channels['OFR'] = -decorrelated_3
    channels['ORL'] = decorrelated_4; channels['ORR'] = -decorrelated_4
    output_12_channels = np.array([channels[name] for name in CHANNEL_ORDER])
    print("Upmixing complete.")
    return output_12_channels

def apply_dynamics_and_eq(twelve_channel_mix):
    print("Stage 2 & 3: Applying dynamics and EQ...")
    expander = NoiseGate(threshold_db=-40, ratio=2.0, attack_ms=5, release_ms=150)
    imax_eq = HighShelfFilter(cutoff_frequency_hz=3000, gain_db=3.0, q=0.707)
    board = Pedalboard([expander, imax_eq])
    processed_audio = board(twelve_channel_mix, sample_rate=TARGET_SR)
    print("Dynamics and EQ complete.")
    return processed_audio

def get_speaker_positions(radius=10):
    positions = []
    for ch in CHANNEL_ORDER:
        az_deg = CHANNEL_LAYOUT[ch]
        el_deg = 30 if ch == 'TCS' else 45 if ch.startswith('O') else 0
        az_rad, el_rad = np.deg2rad(az_deg), np.deg2rad(el_deg)
        x = radius * np.cos(el_rad) * np.sin(az_rad)
        y = radius * np.cos(el_rad) * np.cos(az_rad)
        z = radius * np.sin(el_rad)
        positions.append([x, y, z])
    return positions


# --- IR生成関数をキャッシュ対応に改造 ---
def generate_imax_ir_cached(sr, n_samples):
    """
    pyratoを使用してIRを生成し、結果をキャッシュする。
    キャッシュが存在する場合はそれを読み込む。
    """
    if os.path.exists(IR_CACHE_PATH):
        print(f"Loading cached Impulse Response from {IR_CACHE_PATH}...")
        ir_data = np.load(IR_CACHE_PATH)
        if ir_data.shape == (12, n_samples):
            return ir_data
        else:
            print("Cached IR has incorrect shape. Regenerating...")

    print("Generating synthetic 12-channel Impulse Response using pyrato...")
    room_dim = [25, 35, 18]
    listener_pos = [room_dim[0] / 2, room_dim[1] * 0.6, 2]
    speaker_positions = get_speaker_positions(radius=12)
    target_rt60 = 0.45

    irs = []
    for i in tqdm(range(len(speaker_positions)), desc="Generating IRs"):
        pos = speaker_positions[i]
        rir, _ = ra.analytic.rectangular_room_rigid_walls(
            room_dim, pos, listener_pos,
            reverberation_time=target_rt60, max_freq=2000,
            n_samples=n_samples, samplingrate=sr, speed_of_sound=343
        )
        irs.append(rir.time)

    ir_data = np.vstack(irs)
    np.save(IR_CACHE_PATH, ir_data)
    print(f"Generated and cached synthetic IR with shape {ir_data.shape}")
    return ir_data

# --- 並列処理用のヘルパー関数を追加 ---
def convolve_channel(audio_ch, ir_ch):
    """単一チャンネルの畳み込みを行う関数"""
    if len(ir_ch) > len(audio_ch):
        ir_ch = ir_ch[:len(audio_ch)]
    return scipy.signal.oaconvolve(audio_ch, ir_ch, mode='same')

# --- 空間化関数を並列処理版に置き換え ---
def spatialize_with_ir_parallel(twelve_channel_mix):
    """
    ステージ4: 畳み込みリバーブで空間化する (並列処理版)
    """
    print("Stage 4: Applying spatialization with convolution (in parallel)...")
    
    # 1. マルチチャンネルIRをキャッシュから読み込み、または生成
    ir_samples = int(TARGET_SR * 0.5)
    imax_ir = generate_imax_ir_cached(TARGET_SR, n_samples=ir_samples)
    
    if imax_ir is None:
        print("IR generation failed. Aborting spatialization.")
        return twelve_channel_mix # エラー時は元の音声を返す

    # 2. 畳み込み処理を並列で実行
    tasks = [(twelve_channel_mix[i], imax_ir[i]) for i in range(12)]
    
    num_processes = cpu_count()
    print(f"Starting convolution on {num_processes} CPU cores...")
    
    with Pool(processes=num_processes) as pool:
        results = list(tqdm(pool.starmap(convolve_channel, tasks), total=12, desc="Convolving channels"))
        
    spatialized_audio = np.array(results)
    print("Spatialization complete.")
    return spatialized_audio

# --- サブベース抽出関数 (変更なし) ---
def extract_sub_bass(twelve_channel_mix):
    print("Final Stage: Extracting sub-bass using 4th-order Linkwitz-Riley crossover...")
    crossover_freq = 80
    
    # SOS (Second-Order Sections) 形式を使う方が数値的に安定している
    sos_lp = scipy.signal.butter(4, crossover_freq, 'low', fs=TARGET_SR, output='sos')
    sos_hp = scipy.signal.butter(4, crossover_freq, 'high', fs=TARGET_SR, output='sos')
    
    num_channels, num_samples = twelve_channel_mix.shape
    
    final_12_channels = np.zeros_like(twelve_channel_mix)
    sub_bass_channel = np.zeros(num_samples, dtype=np.float32)
    
    # tqdmで進捗を表示
    for i in tqdm(range(num_channels), desc="Applying bass management"):
        audio_ch = twelve_channel_mix[i, :]
        
        # ローパスフィルターを適用
        low_passed = scipy.signal.sosfilt(sos_lp, audio_ch)
        sub_bass_channel += low_passed
        
        # ハイパスフィルターを適用
        high_passed = scipy.signal.sosfilt(sos_hp, audio_ch)
        final_12_channels[i, :] = high_passed
        
    print("Sub-bass extraction complete.")
    return final_12_channels, sub_bass_channel

# --- メインパイプラインを改造 ---
def process_to_imax(input_path, output_path):
    """
    IMAX変換処理のメインパイプライン (高速化版)
    """
    stereo_waveform = load_audio(input_path)
    if stereo_waveform is None:
        return

    twelve_channel_mix = upmix_to_12_channels(stereo_waveform)
    processed_channels = apply_dynamics_and_eq(twelve_channel_mix)
    
    # 並列処理版の空間化関数を呼び出す
    spatialized_audio = spatialize_with_ir_parallel(processed_channels)

    final_12_channels, sub_bass_channel = extract_sub_bass(spatialized_audio)
    save_multichannel_wav(output_path, final_12_channels, sub_bass_channel)

# --- main関数 (変更なし) ---
def main():
    parser = argparse.ArgumentParser(description="Convert a stereo WAV file to an IMAX-like 12.1 channel experience.")
    parser.add_argument("input_file", help="Path to the input stereo WAV file.")
    parser.add_argument("output_file", help="Path to save the output 12.1 channel WAV file.")
    args = parser.parse_args()
    process_to_imax(args.input_file, args.output_file)

if __name__ == "__main__":
    main()