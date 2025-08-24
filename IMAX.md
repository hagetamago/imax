# IMAXイマーシブサウンド体験の計算論的エミュレーション: 方法論的青写真

## 第1章 IMAX音響アーキテクチャの解剖

IMAXの独特な音響体験は、単一のエフェクトや特定の音響処理技術の産物ではなく、コンテンツ制作から劇場での再生に至るまで、あらゆる変数が厳密に管理されたエンドツーエンドのエコシステムの特性として現れる。本章では、この音響アーキテクチャをその基本理念から物理的な構成要素に至るまで分解し、その特異性を生み出す核心的要素を特定する。

### 1.1 制御という哲学:エンドツーエンドの音響エコシステム

IMAXの音響設計における基本理念は「完全な制御」である。これは、様々な劇場形状やスピーカーレイアウトへの適応性を前提とするDolby Atmosのようなフォーマットとは対照的である¹。IMAXのサウンドは、あらかじめ定義され、標準化された音響環境のために特別にミキシングされる。これにより、認定されたどの劇場においても一貫した音響体験が保証される³。

このエコシステムの出発点は、劇場に音声が届く前の段階、すなわちデジタル・メディア・リマスタリング(DMR)プロセスにある⁵。映画のオリジナルサウンドトラック(通常、台詞、音楽、効果音などのステムで構成される)は、IMAX独自のスピーカー構成と広大なダイナミックレンジ能力に合わせて、専門のチームによって再ミキシングおよびマスタリングされる。このDMRプロセスには、IMAXの大画面フォーマットに合わせて画像のノイズや粒子感を最適に低減し、明瞭度を向上させるための独自のアルゴリズムが含まれており、音響面でも同様の思想が貫かれている⁶。この特注のミキシングこそが、IMAXサウンドを一般的な劇場用ミックスから根本的に区別する第一の要因である。

### 1.2 イマージョンの解剖学:プロポーショナル・ポイントソース・ラウドスピーカー

IMAXサウンドの物理的な発信源であるスピーカーシステムは、その音響哲学を具現化したものである。拡散的な音場を創出するために多数の小型スピーカーをアレイ状に配置する従来の多くの劇場とは異なり、IMAXは少数の大型で高出力な「ポイントソース(点音源)」スピーカーを採用している²。ここでの目標は音の拡散ではなく、極めて高い明瞭度と正確なインパルス応答を持つ、指向性の明確なサウンドを届けることにある¹¹。

この思想を技術的に実現するのが、IMAX独自の「プロポーショナル・ポイントソース(PPS)」スピーカーである。このスピーカーの最大の特徴は、フレア率(ホーンの開口部の広がり率)が可変な特殊設計のホーンにある。IMAXシアターの客席は、従来のものより急勾配で高さがあるという特徴的な形状を持つが¹²、このPPSスピーカーは、そのような空間のどの座席にも均一な音圧レベル(SPL)を届けるように設計されている²。この音響工学的な工夫により、極めて広く安定した「スイートスポット」が生まれ、観客は座席位置に関わらず一貫した音響体験を得ることができる²。また、その台形の指向性パターンは、IMAXオーディトリアムの独特な形状に合致するように特別に設計されている¹⁰。

さらに、IMAXシステムの決定的かつ根本的な特徴として、サラウンドスピーカーを含むシステム内のすべてのスピーカーがフルレンジである点が挙げられる³。これは、各スピーカーが重低音から高音域まで、非常に広い周波数帯域を再生可能であることを意味する。サラウンドスピーカーの再生帯域が制限されている従来のシステムとは一線を画すこの設計思想は、後述する独自の低音管理システムの前提条件となっている。これらのスピーカーはIMAXのためにカスタム製造されており、歴史的にはJBL、Yorkville Audio、Danley Sound Labsといったハイエンドオーディオメーカーのコンポーネントが採用されてきた¹³。

### 1.3 パワーの源泉: 12チャンネルレイアウトとLFEレス・サブベースシステム

IMAXの音響システムは時代と共に進化してきた。初期のシステムは、スクリーン背後のレフト、センター、ライト、後方のレフトリア、ライトリア、そしてスクリーン上部に設置されたユニークな「ボイス・オブ・ゴッド」チャンネルからなる6チャンネル構成であった¹⁰。最新のIMAX with Laserシステムでは、これが12チャンネルのディスクリート(独立した)チャンネルベースシステムへと拡張されている²。ここで重要なのは、劇場での実装において、これがDolby AtmosやDTS:Xのようなオブジェクトベースのオーディオではないという点である¹。

複数の情報源を統合すると、現代の12チャンネル構成は以下のように整理できる。

*   **スクリーンチャンネル (4ch):** レフトスクリーン (LS)、センタースクリーン (CS)、ライトスクリーン(RS)、そして「ボイス・オブ・ゴッド」の進化形であるトップセンタースクリーン (TCS) ¹⁶。
*   **サイドサラウンド (2ch):** レフトサイド (LSi)、ライトサイド (RSi)。客席中ほどの側壁に配置される¹⁶。
*   **リアサラウンド (2ch):** レフトリア (LR)、ライトリア (RR)。客席後方のコーナーに配置される ¹⁶。
*   **オーバーヘッドチャンネル (4ch):** 前方2つ (OFL, OFR) と後方2つ (ORL, ORR) の天井埋め込み型スピーカー ¹⁶。

そして、従来のサウンドデザインからの最も根本的な逸脱は、オーディオミックスに専用のLFE(Low-Frequency Effects)チャンネル、すなわち`.1`チャンネルが存在しないことである²⁰。その代わりに、低周波成分は劇場に設置されたプロセッサー内のクロスオーバーフィルターを介して、12チャンネルすべてのフルレンジチャンネルから抽出される。この抽出され、合計された低音信号が、スクリーン背後に設置された独立した巨大なサブベース・スピーカーアレイに送られる³。このアレイは、-3dBポイントで20Hzという超低域までを、絶大なパワー(古いシステムでもサブベースだけで3000ワット以上と報告されている)で再生する能力を持つ³。

このアプローチは、低音が単なる「効果音」ではなく、音風景全体を構成する豊かで実体的な要素として扱われることを保証する。サラウンドスピーカーを含む全てのスピーカーがフルレンジでなければ、それらのチャンネルから意味のある低周波情報を抽出することは不可能である。つまり、IMAXミックスにおける音のオブジェクトは、空間内を移動する際に自身の完全な周波数スペクトルを保持しており、LFEを別個のエンティティとして扱うシステムとはパラダイムが根本的に異なる。これが、IMAX特有の身体を揺さぶるような内臓感覚的な重低音体験の源泉となっている³。

**表1: IMAX 12チャンネルスピーカーレイアウトと公称配置**

本エミュレーションの目標となる音場を定義するため、以下に最新の12チャンネルシステムの理想的なスピーカー配置をまとめる。角度はリスニングポイント中央を原点とし、正面を方位角0°、水平面を仰角0°とする。

| チャンネル名 | 略称 | 方位角 (Azimuth) | 仰角 (Elevation) |
| :--- | :--- | :--- | :--- |
| Left Screen | LS | -30° | 0° |
| Center Screen | CS | 0° | 0° |
| Right Screen | RS | +30° | 0° |
| Top Center Screen | TCS | 0° | +30°~+45° |
| Left Side | LSi | -90° | 0° |
| Right Side | RSi | +90° | 0° |
| Left Rear | LR | -135° | 0° |
| Right Rear | RR | +135° | 0° |
| Overhead Front Left | OFL | -45° | +45° |
| Overhead Front Right | OFR | +45° | +45° |
| Overhead Rear Left | ORL | -135° | +45° |
| Overhead Rear Right | ORR | +135° | +45° |

## 第2章 音響環境の定量化

IMAXシアターの物理的特性を、デジタル実装可能な一連の定量化可能なパラメータに変換する。本章の目的は、主に合成マルチチャンネル・インパルス応答(IR)の生成を通じて、仮想的な音響モデルを構築することである。

### 2.1 音響キャンバスの設計:音響処理と遮音基準

IMAXシアターは音響的に「デッド」になるように設計されている²²。これは、壁や天井からの音の反射を最小限に抑え、非常に短い残響時間を持つことを意味する。その目的は、観客が部屋自体によって着色されていない、スピーカーからの直接音を聴くことにある²²。正確なRT60(残響時間)の値は公開されていないが、その設計思想はコンサートホールよりも大幅に短い値、おそらく0.4秒から0.6秒の範囲で、特に低周波の減衰制御に重点を置いていることを示唆している。

さらに、認定には極めて低い環境騒音レベルが要求される。「一般的な映画館のレベルであるNC-35よりもはるかに優れている」と規定されており²²、例えばロンドンのBFI IMAXはNC-25という非常に静かな基準を満たすように設計されている。これを達成するためには、近隣の地下鉄トンネルからの振動を遮断するなど、大規模な防振対策が必要となる²⁴。劇場は「ボックス・イン・ボックス」構造で建設され、システムの広大なダイナミックレンジが外部の妨害によって損なわれないよう、高い遮音性能が確保されている²²。

### 2.2 「秘伝のタレ」:独自のイコライゼーションと自動キャリブレーション

標準的な映画館は、通常、ISO 2969規格の「Xカーブ」に合わせてイコライジングされる。このカーブは、$2 \text{ kHz}$から高周波のロールオフ(減衰)を導入するものである ²⁷。IMAXはこの標準を明確に拒否している。彼らは40年以上にわたって開発された独自のカスタムEQカーブを利用しており、これはXカーブのような高周波減衰を伴わない、よりフラットな周波数応答に近いと報告されている³。

この背景には、IMAXシステムの設計思想そのものがある。Xカーブは、旧来のフィルム音声フォーマットやスピーカーアレイの累積的な高周波応答を補正し、残響の多い空間で高音がきつく聞こえるのを和らげるために開発された側面がある²⁸。対照的に、IMAXは非圧縮デジタル音声、カスタム設計のフルレンジスピーカー、そして音響的にデッドな室内環境という、システム全体を制御している ³。高周波の歪みや制御不能な残響の原因が設計段階で排除されているため、Xカーブによる補正的なロールオフの必要性自体が存在しない。したがって、IMAXのよりフラットなEQカーブは単なる好みではなく、優れたエンドツーエンドシステム設計の論理的な帰結である。

すべての劇場がこの独自のカーブに準拠することを保証するため、IMAXはNEXOSと呼ばれる自動チューニングシステムを採用している。このシステムは、オーディトリアム内に恒久的に設置された多数のマイクを使用してリアルタイムの音響データを収集する³。そして、IMAXが映画館での独占使用権を持つ、Audyssey MultEQアルゴリズムを大幅に改良したバージョンを用いて精密なイコライゼーションを適用し、各部屋固有の音響特性を補正してターゲットカーブへの準拠を徹底する³。システムは、85 dBc SPLを基準レベルとしてキャリブレーションされる⁴。

### 2.3 空間の合成: 仮想IMAXインパルス応答(IR)のモデル

実際のIMAXシアターから測定されたIRは専有情報であり入手不可能なため、計算によって合成マルチチャンネルIRを生成する必要がある。このIRは音響空間のデジタルな指紋であり、後段の畳み込みリバーブ処理に不可欠である。

IRは音響モデリングの原理を用いて生成される。まず、大規模なIMAXシアターの典型的な寸法(例:25m×35m×18m)を持つ仮想空間をモデル化する¹²。次に、前述のパラメータ(短いRT6O、音響処理された壁面の特定の吸音係数など)を用いて、イメージソース法やレイトレーシング法などのアルゴリズムを使い、12個の各スピーカー位置から中央のリスニングポイントまでの音の反射をシミュレートする。このプロセスを12のソースチャンネルすべてに対して繰り返し、12チャンネルのIRファイルを生成する。このファイルは、残響特性だけでなく、空間認識の基礎となるチャンネル間の極めて重要なタイミングとレベル差(両耳間時間差・レベル差 - ITD/ILD)を捉える。

ここで重要なのは、IMAXシアターが「音響的にデッド」であるという事実である。したがって、本シミュレーションにおける畳み込みIRの主な役割は、豊かな残響を付加することではない。その目的はより繊細であり、広大な物理的空間を定義する初期反射と、正確な時間・レベル情報を精密にモデル化することにある。目標は、IMAXのクリアでダイレクトなサウンド哲学と矛盾するような、耳につく「部屋鳴り」を加えることなく、包囲感とスケール感を生み出すことである。したがって、合成IRは、強い直接音、広大な部屋の寸法に対応する疎だが明確な初期反射パターン、そして非常に速く非拡散的な減衰テールによって特徴づけられる必要がある。この畳み込み処理は、「リバーブを加える」というよりは、「音声を特定の、制御された、広大な音響スナップショットの中に配置する」という行為に近い ²⁹。

**表2: IMAXエミュレーションのための目標音響パラメータ**

仮想空間モデルの構築とDSPアルゴリズムの設計における具体的な目標値を以下に示す。

| 音響メトリクス | 目標値/設計方針 |
| :--- | :--- |
| 残響時間 (RT60) | 全帯域で短く、特に低域の減衰を制御。目標: $1 \text{ kHz}$で < 0.5秒 |
| 背景騒音 | NC-25 (Noise Criterion 25) |
| 周波数応答 (EQカーブ) | Xカーブの高周波ロールオフなし。目標: $20 \text{ Hz} \sim 18 \text{ kHz}$の範囲で$\pm1.5 \text{ dB}$以内のフラットな応答 |
| IR特性 | 強い直接音、疎で明確な初期反射、急速な減衰テール |

## 第3章 IMAXエミュレーションのためのデジタル信号処理チェーン

本章では、ソースとなるオーディオファイルを目標とするIMAXエミュレーションに変換するための一連のDSPアルゴリズムのパイプラインを段階的に提示する。各ステージは前章までに確立された原則によって正当化され、具体的なアルゴリズムが提案される。

### 3.1 ステージ1: アップミックス - ステレオから12チャンネル音場へ

最も一般的な入力フォーマットである2チャンネルステレオソースから、一貫性のある没入型の12チャンネル音場を生成することが目的である。これは、元の信号には存在しない情報を生成するため、本プロセスの中で最も複雑かつ推測的な段階となる。

#### 3.1.1 直接音と環境音の信号分離原理

インテリジェントなアップミックスの第一歩は、ステレオ信号をその構成要素、すなわち「直接音」(台詞やリード楽器のような相関性の高い、パンニングされた要素)と「環境音」(リバーブや群衆のノイズのような無相関で拡散的な要素)に分離することである³⁰。この分離により、これらのコンポーネントをサラウンドフィールド内で別々に処理し、配置することが可能になる。

#### 3.1.2 アルゴリズム1:位相振幅マトリックス・アップミックス(耳レベルチャンネル用)

これは、センター(C)、レフトサラウンド(LS)、ライトサラウンド(RS)チャンネルを生成するための古典的な手法である。映画音響では台詞や主要なアクションはスクリーンチャンネルに定位するため、このフロントステージを正確に構築することが最も重要である。

*   **センターチャンネル (C):** C=a・(L+R)。センターチャンネルは、ステレオ信号の同相で相関性の高い成分から抽出される。係数aは通常、等しいパワーを維持するために約0.707に設定される³²。
*   **フロントL/R (L'/R'):** 元のL/R信号はフロントチャンネルとして維持されるが、分離を強化するために抽出されたセンターチャンネル成分を部分的に差し引くことができる(例:L'=L-b・C)。
*   **サラウンドチャンネル (LS/RS):** これらは逆相で逆相関の情報から抽出される。$LS/RS = c \cdot (L - R)$の形式をとり、空間感覚を強調しコムフィルタリングを防ぐために、しばしばわずかな遅延(10-20ms)や位相シフト(例:ヒルベルト変換)が適用される³²。

#### 3.1.3 アルゴリズム2:デ相関とパンニング(サイド/ハイトチャンネル用)

残りのチャンネル(サイドサラウンド、オーバーヘッド、トップセンター)は、主にアンビエンスと包囲感のために使用される。これらは、抽出された環境音(または派生したサラウンド信号)をさらに処理することで生成できる。

*   **デ相関(Decorrelation):** 音の単純な「コピー」を避けるため、信号をデ相関させる必要がある。これは、短くランダムに変化するオールパスフィルターや、ベルベットノイズのような疎なノイズシーケンスとの畳み込みによって達成できる³⁶。これにより、脳がより広く拡散した音場として知覚する、似ているが異なる2つの信号が生成される。
*   **パンニングと遅延:** デ相関された環境音信号は、表1で定義されたサイド、オーバーヘッド、トップセンターチャンネルの特定の位置にパンニングされ、リスナーからの距離に基づいて適切な遅延が適用されることで、一体感のある3Dサウンドドームが形成される。

### 3.2 ステージ2: ダイナミックレンジ伸張 - 劇場でのインパクトの復元

ほとんどの家庭用メディアに存在するダイナミックレンジ圧縮を打ち消し、IMAXの劇場用ミックスに特徴的な広大なダイナミックレンジを復元することが目的である³。IMAXは従来のシステムの「10倍のダイナミックレンジ」を謳っており³、これは非常に高いピーク対平均比を示唆している。劇場用ミックスは、制御された環境で85dBcという基準音量で聴かれることを前提に設計されており、最大118dBのピークまで歪みなく再生できる³。この圧縮を逆転させることが目標である。

#### アルゴリズム3: マルチバンド・ダウンワード・エキスパンダー

単純なブロードバンドエキスパンダーはミックス全体に不自然な影響を与える可能性があるため、より洗練されたマルチバンド・エキスパンダーを用いる。

*   **プロセス:** 12の各チャンネルのオーディオ信号を複数の周波数帯域(例:低域、中域、高域)に分割し、各帯域に個別のダウンワード・エキスパンダーを適用する。
*   **パラメータ:**
    *   スレッショルド: 比較的高く設定し、このレベル以下の信号を減衰させる。
    *   レシオ: 1:1.5から1:2.5程度の緩やかな比率で、大きな音と小さな音の差を拡大する。
    *   アタック/リリース: トランジェント(過渡的な音)を損なわないようアタックタイムは速く、ポンピング(音量が不自然に変動する現象)を防ぐためリリースタイムは中程度に設定する。この処理の核心は、エンベロープ検出器とゲインコンピュータにある⁴⁰。

### 3.3 ステージ3: イコライゼーション - 独自のIMAXターゲットカーブの適用

IMAXシステムの音色バランスを定義する、Xカーブではない独自の周波数応答を適用することが目的である。

#### アルゴリズム4: パラメトリック&FIRフィルターのカスケード設計

正確なカーブは専有情報であるため、「可能な限りフラット」であり、標準的な高周波ロールオフがない³という記述に基づいてモデル化する。

*   **実装:** デジタルフィルターをカスケード接続して使用する。広範な音色形成にはパラメトリックイコライザー(ピーキング、シェルビング)を使用し、より精密な制御のためには、窓関数法(例:FIRLSアルゴリズム)を用いて設計された有限インパルス応答(FIR)フィルターを使用し、ターゲット周波数応答を高精度で再現する。ターゲットは、$20 \text{ Hz}$から約$18 \text{ kHz}$までのフラットな応答であり、Xカーブモデルとは大きく異なる²⁷。

### 3.4 ステージ4: 空間化 - マルチチャンネル畳み込みリバーブ

処理された12チャンネルの音声を、第2章で定義した仮想音響空間内に配置することが目的である。

#### アルゴリズム5: 分割畳み込み(オーバーラップアド/セーブ法)

数分間のオーディオファイルと短いマルチチャンネルIRとの直接畳み込みでさえ、計算コストが非常に高くなる⁴³。解決策は分割畳み込みである。

*   **プロセス:** 各チャンネルの入力音声を小さなブロックに分割する。マルチチャンネルIRも対応するブロックに分割する。各オーディオブロックは、FFTベースの高速畳み込み(FFT(audio_block) * FFT(ir_block))を用いてIRのブロックと畳み込まれる。結果として得られる出力ブロックは、オーバーラップアド法またはオーバーラップセーブ法を用いてつなぎ合わされ、シームレスで連続的な出力ストリームが生成される⁴⁵。これにより、リアルタイムまたはそれに近い処理が可能になる。

ここで、家庭用AVレシーバーにおける「IMAX Enhancedモード」の挙動は、我々のモデルにとって重要なヒントを提供する²¹。このモードはユーザーの低音管理設定を上書きし、顕著な低音ブーストを適用する。これは、劇場での強烈なSPLと空気の振動によって生み出される身体的な低音感覚を、家庭のより低い再生音量で心理音響的に補償するためのものである可能性が高い。人間の聴覚は、フレッチャー・マンソン曲線が示すように、低音量では低周波数に対する感度が低下する。IMAX EnhancedのDSPは、この知覚的な不足を補うために、ダイナミックEQやローシェルフブーストを適用していると考えられる。したがって、本Pythonモデルには、この「IMAX Enhancedモード」をエミュレートする、オプションの最終段ダイナミックEQまたは低音ブースト機能を含めるべきである。

## 第4章 Python実装の青写真

本章では、理論的なDSPチェーンを実用的なPythonアプリケーションに変換するための具体的なガイダンスを提供する。ツール選定、コードアーキテクチャ、そしてユーザー向けの制御項目に焦点を当てる。

### 4.1 ツールキットの選定: Pythonオーディオライブラリの比較分析

タスクに適したライブラリを選択することは、パフォーマンスと開発効率の両面で極めて重要である。

*   **コア処理 (SciPy, NumPy):** フィルター設計 (scipy.signal.iirfilter, scipy.signal.firwin)、フィルター適用 (scipy.signal.lfilter, scipy.signal.oaconvolve)、FFT (scipy.fft) といった基本的なDSPタスクには、これらのライブラリが業界標準である。NumPyは、すべての数値配列操作に不可欠である⁴⁸。
*   **高レベル抽象化 (Pedalboard):** SpotifyのPedalboardは、処理チェーンを構築する上で優れた選択肢である。圧縮/伸張、EQなどの一般的なエフェクトが、高度に最適化されたC++実装として提供されており、Pythonicな方法で連結できる。GIL(グローバルインタプリタロック)を解放する能力により、マルチコア処理において非常に高速である⁵¹。
*   **専門的な音響処理 (pyfar):** 合成インパルス応答の生成と操作というタスクには、pyfarが音響分析と畳み込みのための専門的なツールを提供しており、SciPyでゼロから実装するよりも直接的である可能性がある⁴⁵。
*   **ファイルI/Oとリサンプリング (librosa, torchaudio):** SciPyもWAVファイルを読み込めるが、librosaやtorchaudioのようなライブラリは、様々なオーディオフォーマットのより堅牢な扱いや、高品質なリサンプリングアルゴリズムを提供しており、入力ファイルをプロジェクトの内部サンプルレートに標準化するために必要となる⁵²。
*   **推奨アプローチ:** ハイブリッドアプローチが最適である。低レベルでカスタムなアルゴリズム開発(アップミキサー、IR生成)にはNumPy/SciPyを使用し、これらのカスタムコンポーネントをPedalboardの高性能なエフェクトと連結することで、パフォーマンスと使いやすさを両立させる。ファイル入力にはlibrosaの堅牢性を活用する。

**表3: Pythonオーディオライブラリの適合性マトリックス**

| DSPタスク | librosa | SciPy | Pedalboard | pyfar |
| :--- | :--- | :--- | :--- | :--- |
| ファイルI/O | 非常に良い | 良い (WAVのみ) | 良い | 良い |
| リサンプリング | 非常に良い | 良い | 非常に良い | - |
| フィルタリング (IIR/FIR) | - | 非常に良い | 非常に良い | 良い |
| STFT / FFT | 非常に良い | 非常に良い | - | 良い |
| ダイナミクス処理 | - | - | 非常に良い | - |
| 畳み込み | 良い | 非常に良い | - | 非常に良い |

### 4.2 コードロジックと高レベル構造

主要な処理関数の高レベルな疑似コードを以下に示す。

```python
import librosa
import numpy as np
import scipy.signal
# Pedalboardやpyfarなどの他のライブラリもインポート

def process_to_imax(audio_file_path, parameters):
    # 1. 読み込みと前処理
    # librosaを使用してファイルを読み込み、48kHzにリサンプリング
    waveform, sample_rate = librosa.load(audio_file_path, sr=48000, mono=False)
    assert waveform.shape == 2, "Input must be a stereo file."

    # 2. ステージ1: アップミックス
    # 直接音と環境音に分離
    direct_signal, ambient_signal = decompose_stereo(waveform)
    # マトリックスアップミックスで耳レベルチャンネルを生成
    lcr_channels = matrix_upmix(direct_signal)
    # デ相関を用いてサラウンド、サイド、ハイトチャンネルを生成
    surround_channels = generate_surrounds(ambient_signal)
    height_side_channels = generate_height_sides(ambient_signal)
    # 12チャンネルのミックスを結合
    twelve_channel_mix = combine_channels(lcr_channels, surround_channels,
    height_side_channels)

    # 3. ステージ2 & 3: チャンネルごとのダイナミクスとEQ
    processed_channels = []
    for channel_data in twelve_channel_mix:
        # ダイナミックレンジ伸張
        expanded_channel = expander.process(channel_data, parameters['expansion'])
        # IMAXターゲットカーブを適用
        eq_channel = imax_eq.process(expanded_channel, parameters['eq'])
        processed_channels.append(eq_channel)

    # 4. ステージ4: 空間化
    # 合成IRを読み込みまたは生成
    synthetic_ir = load_or_generate_ir(parameters['room_acoustics'])
    # 分割畳み込みを実行
    spatialized_audio = partitioned_convolve(processed_channels, synthetic_ir)

    # 5. 最終ステージ: サブベース抽出
    # 全チャンネルから低域を抽出し、合計してサブベースチャンネルを作成
    final_12_channels, sub_bass_channel = extract_sub_bass(spatialized_audio)

    # 6. 出力
    # 12.1チャンネルのWAVファイルとして保存
    save_multichannel_wav(final_12_channels, sub_bass_channel)
    return True
```

### 4.3 パラメータ化とユーザーコントロール

ツールを柔軟にするため、各ステージの主要なパラメータをユーザーに公開し、調整と実験を可能にする。

*   **アップミックス:** 「フロント/リアバランス」や「アンビエンス幅」(デ相関レベルを制御)などのコントロール。
*   **ダイナミクス:** エキスパンダーのスレッショルド/レシオを制御する単一の「シアターインパクト」ノブ。
*   **空間化:** 畳み込みリバーブの「ルームサイズ」または「ウェット/ドライ」ミックスコントロール。
*   **心理音響:** 家庭でのリスニング用に「IMAX Enhancedモード」の低音ブーストを切り替えるトグル。

## 第5章 最終考察と発展的トピック

本章では、処理チェーンの最後の重要なステップを取り上げ、プロジェクトに内在する限界について議論するとともに、将来のより高度な開発への道筋を示す。

### 5.1 サブベースシステムの再現

すべての処理が完了した後、IMAXの`.0`アーキテクチャを正確にモデル化する最終ステップとして、低音管理を行う。

#### アルゴリズム6: ベースマネジメントとサミング

*   **プロセス:** 処理および空間化された12チャンネルのそれぞれに、クロスオーバー周波数が約80 Hzのローパスフィルター(例:4次リンクウィッツ・ライリーフィルター)を適用する。
*   **サミング:** フィルター処理された12チャンネルすべての低周波信号を合計し、単一のモノラルチャンネルを生成する。
*   **ハイパス:** 元の12チャンネルには対応するハイパスフィルターを適用し、メインスピーカーとサブウーファーで低音域が重複して再生されることによる位相問題を回避する。
*   **出力:** プログラムの最終的な出力は13チャンネルのオーディオとなる。すなわち、ハイパス処理された12のメインチャンネルと、合計された1つのサブベースチャンネルである。これにより、IMAXシステムのアーキテクチャが忠実にモデル化される ¹³。

### 5.2 限界と今後の研究への展望

本報告書で提案されたアプローチは、物理学と音響工学の原理に基づいたIMAXサウンド体験の忠実なエミュレーションを目指すものであるが、いくつかの本質的な限界が存在する。

*   **アップミックス問題:** アップミックスは、根本的に「情報に基づいた推測」の行為である。ソースには存在しない空間情報を生成しているため、提案されたアルゴリズムが音響心理学の原理に基づいていても、サウンドデザイナーがオリジナルのマルチトラックステムから作成したディスクリート12チャンネルミックスを完全に再現することはできない。
*   **専有情報:** IMAXのEQカーブの正確なパラメータ、NEXOSキャリブレーションアルゴリズム、PPSラウドスピーカーの精密な内部構造は企業秘密である。我々のモデルは、入手可能な公開情報に基づく、高度に教育された近似である。
*   **高度な技術 - AIと伝達関数モデリング:** 将来、さらに高い精度を達成するための有望な方向性として、深層学習の活用が考えられる。例えば、公式予告編などで公開されている数少ないIMAX音声サンプルと、それに対応する標準的なステレオバージョンをペアとして、ニューラルネットワーク(例:U-NetやCNN)を訓練させることが可能である⁵⁴。ネットワークは、DMR、ダイナミクス、EQ、空間化を含むIMAX処理チェーン全体の複雑で非線形な伝達関数を学習する可能性があり、本報告書で概説したモジュール式のDSPアプローチよりも、より正確で包括的なモデルを構築できるかもしれない。

### 引用文献

1.  IMAX and Dolby Atmos : r/imax - Reddit, 8月 24, 2025にアクセス、[https://www.reddit.com/r/imax/comments/1aex0qw/imax_and_dolby_atmos/](https://www.reddit.com/r/imax/comments/1aex0qw/imax_and_dolby_atmos/)
2.  IMAX Reveals New 12-Track Audio Solution – Display Daily, 8月 24, 2025にアクセス、[https://displaydaily.com/29imax-reveals-new-12-track-audio-solution/](https://displaydaily.com/29imax-reveals-new-12-track-audio-solution/)
3.  The sound of IMAX | Home Cinema Choice, 8月 24, 2025にアクセス、[https://www.homecinemachoice.com/content/sound-imax](https://www.homecinemachoice.com/content/sound-imax)
4.  Anyone want to discuss IMAX theater system playback sound? : r/audioengineering - Reddit, 8月 24, 2025にアクセス、[https://www.reddit.com/r/audioengineering/comments/41qh42/anyone_want_to_discuss_imax_theater_system/](https://www.reddit.com/r/audioengineering/comments/41qh42/anyone_want_to_discuss_imax_theater_system/)
5.  Straight talking guides to IMAX enhanced - Sound Advice, 8月 24, 2025にアクセス、[https://www.sound-advice.online/guides/imax-enhanced](https://www.sound-advice.online/guides/imax-enhanced)
6.  IMAX® 101 DMR - YouTube, 8月 24, 2025にアクセス、[https://www.youtube.com/watch?v=yICDPszuar8](https://www.youtube.com/watch?v=yICDPszuar8)
7.  The Ultimate Guide to IMAX Sound - Number Analytics, 8月 24, 2025にアクセス、[https://www.numberanalytics.com/blog/the-ultimate-guide-to-imax-sound](https://www.numberanalytics.com/blog/the-ultimate-guide-to-imax-sound)
8.  IMAX Enhanced: what is it, how do you get it and is it any good? - What Hi-Fi?, 8月 24, 2025にアクセス、[https://www.whathifi.com/advice/imax-enhanced-what-is-it-how-do-you-get-it-and-is-it-any-good](https://www.whathifi.com/advice/imax-enhanced-what-is-it-how-do-you-get-it-and-is-it-any-good)
9.  How can you remaster a movie for IMAX that hasn't been shot originally on that format?, 8月 24, 2025にアクセス、[https://www.reddit.com/r/blankies/comments/1bg1g0g/how_can_you_remaster_a_movie_for_imax_that_hasnt/](https://www.reddit.com/r/blankies/comments/1bg1g0g/how_can_you_remaster_a_movie_for_imax_that_hasnt/)
10. IMAX film format, 8月 24, 2025にアクセス、[http://sunnycv.com/steve/filmnotes/imax.html](http://sunnycv.com/steve/filmnotes/imax.html)
11. PART III: Point Source vs Line Array and Introduction to VHD5.0 – KV2 Audio, 8月 24, 2025にアクセス、[https://www.kv2audio.com/technical-talks-with-george-krampera/part-iii-point-source-vs-line-array-and-introduction-to-vhd50.html](https://www.kv2audio.com/technical-talks-with-george-krampera/part-iii-point-source-vs-line-array-and-introduction-to-vhd50.html)
12. IMAX - Wikipedia, 8月 24, 2025にアクセス、[https://en.wikipedia.org/wiki/IMAX](https://en.wikipedia.org/wiki/IMAX)
13. Imax Sound System - In 70mm, 8月 24, 2025にアクセス、[https://www.in70mm.com/presents/1970_imax/library/sound/index.htm](https://www.in70mm.com/presents/1970_imax/library/sound/index.htm)
14. About the IMAX Speakers, which Manufacturer made them? - Reddit, 8月 24, 2025にアクセス、[https://www.reddit.com/r/imax/comments/1hwddl9/about_the_imax_speakers_which_manufacturer_made/](https://www.reddit.com/r/imax/comments/1hwddl9/about_the_imax_speakers_which_manufacturer_made/)
15. Could someone tell me what these IMAX speakers are worth? : r/hometheater - Reddit, 8月 24, 2025にアクセス、[https://www.reddit.com/r/hometheater/comments/185nbgb/could_someone_tell_me_what_these_imax_speakers/](https://www.reddit.com/r/hometheater/comments/185nbgb/could_someone_tell_me_what_these_imax_speakers/)
16. What does the loudspeakers looks like behind the IMAX screen at AMC Lincoln Square - Reddit, 8月 24, 2025にアクセス、[https://www.reddit.com/r/imax/comments/1dj65z3/what_does_the_loudspeakers_looks_like_behind_the/](https://www.reddit.com/r/imax/comments/1dj65z3/what_does_the_loudspeakers_looks_like_behind_the/)
17. Next generation IMAX sound system detailed - Film-Tech Forum ARCHIVE, 8月 24, 2025にアクセス、[https://www.film-tech.com/ubb/f16/t002230.html](https://www.film-tech.com/ubb/f16/t002230.html)
18. What are the audio specs of cinema audio tracks? : r/imax - Reddit, 8月 24, 2025にアクセス、[https://www.reddit.com/r/imax/comments/1dbhln8/what_are_the_audio_specs_of_cinema_audio_tracks/](https://www.reddit.com/r/imax/comments/1dbhln8/what_are_the_audio_specs_of_cinema_audio_tracks/)
19. How is the 12 Channel sound? : r/imax - Reddit, 8月 24, 2025にアクセス、[https://www.reddit.com/r/imax/comments/tiwct0/how_is_the_12_channel_sound/](https://www.reddit.com/r/imax/comments/tiwct0/how_is_the_12_channel_sound/)
20. Here's this video for those who are interested in how IMAX does their sound. - Reddit, 8月 24, 2025にアクセス、[https://www.reddit.com/r/imax/comments/wgm5fw/heres_this_video_for_those_who_are_interested_in/](https://www.reddit.com/r/imax/comments/wgm5fw/heres_this_video_for_those_who_are_interested_in/)
21. IMAX Enhanced Audio Examined, Part 2 - High-Def Digest: The ..., 8月 24, 2025にアクセス、[https://www.highdefdigest.com/blog/imax-enhanced-dts-audio-part-2/](https://www.highdefdigest.com/blog/imax-enhanced-dts-audio-part-2/)
22. Cinema Acoustics for IMAX Theatres | ABD Engineering & Design, 8月 24, 2025にアクセス、[https://www.abdengineering.com/blog/imax-theatre-secrets/](https://www.abdengineering.com/blog/imax-theatre-secrets/)
23. The Soundscape of the Cinema Theatre: Acoustical Design, Embodiment, and Film Theatres as Vehicles for Aural Absorption – Liverpool University Press, 8月 24, 2025にアクセス、[https://www.liverpooluniversitypress.co.uk/doi/pdf/10.3828/msmi.2016.8?download=true](https://www.liverpooluniversitypress.co.uk/doi/pdf/10.3828/msmi.2016.8?download=true)
24. VIBRATION ISOLATION OF THE IMAX CINEMA, WATERLOO, LONDON – Institute of Acoustics, 8月 24, 2025にアクセス、[https://www.ioa.org.uk/system/files/proceedings/p_henson_jg_charles_vibration_isolation_of_the_imax_cineman_waterloo_london.pdf](https://www.ioa.org.uk/system/files/proceedings/p_henson_jg_charles_vibration_isolation_of_the_imax_cineman_waterloo_london.pdf)
25. Cinema Acoustics Magic: Inside IMAX & Dolby Atmos Sound Design - Schallertech, 8月 24, 2025にアクセス、[https://schallertech.com/en/cinema-acoustics/](https://schallertech.com/en/cinema-acoustics/)
26. Acoustics and Design of Movie Theatre | PDF | Curtain – Scribd, 8月 24, 2025にアクセス、[https://www.scribd.com/document/464476934/acousticsanddesignofmovietheatre-170923172912](https://www.scribd.com/document/464476934/acousticsanddesignofmovietheatre-170923172912)
27. Target Room Response and Cinema X-curve | Audio Science Review (ASR) Forum, 8月 24, 2025にアクセス、[https://www.audiosciencereview.com/forum/index.php?threads/target-room-response-and-cinema-x-curve.10/](https://www.audiosciencereview.com/forum/index.php?threads/target-room-response-and-cinema-x-curve.10/)
28. Validity of X-curve For Cinema Sound | Audio Science Review (ASR) Forum, 8月 24, 2025にアクセス、[https://www.audiosciencereview.com/forum/index.php?threads/validity-of-x-curve-for-cinema-sound.204/](https://www.audiosciencereview.com/forum/index.php?threads/validity-of-x-curve-for-cinema-sound.204/)
29. Impulse Response - Studio Six Digital, 8月 24, 2025にアクセス、[https://studiosixdigital.com/audiotools-modules-2/acoustic-analysis-modules/impulse_response/](https://studiosixdigital.com/audiotools-modules-2/acoustic-analysis-modules/impulse_response/)
30. Stereo signal separation and upmixing by mid-side decomposition in the frequency-domain - International Conference on Digital Audio Effects (DAFx), 8月 24, 2025にアクセス、[https://www.dafx.de/paper-archive/2015/DAFx-15_submission_9.pdf](https://www.dafx.de/paper-archive/2015/DAFx-15_submission_9.pdf)
31. Direct-ambient decomposition and upmix of surround signals | Request PDF - ResearchGate, 8月 24, 2025にアクセス、[https://www.researchgate.net/publication/221016707_Direct-ambient_decomposition_and_upmix_of_surround_signals](https://www.researchgate.net/publication/221016707_Direct-ambient_decomposition_and_upmix_of_surround_signals)
32. Procedure for upmixing a stereo audio to a 5.1 channel audio - ResearchGate, 8月 24, 2025にアクセス、[https://www.researchgate.net/figure/Procedure-for-upmixing-a-stereo-audio-to-a-51-channel-audio_fig3_45796449](https://www.researchgate.net/figure/Procedure-for-upmixing-a-stereo-audio-to-a-51-channel-audio_fig3_45796449)
33. Dolby encoding, Dolby Pro Logic Decoding - SOS Forum - Sound On Sound, 8月 24, 2025にアクセス、[https://www.soundonsound.com/forum/viewtopic.php?t=11210](https://www.soundonsound.com/forum/viewtopic.php?t=11210)
34. Surround Sound Matrix Encoding and Decoding - MATLAB & Simulink - MathWorks, 8月 24, 2025にアクセス、[https://www.mathworks.com/help/audio/ug/surround-sound-matrix-encoding-and-decoding.html](https://www.mathworks.com/help/audio/ug/surround-sound-matrix-encoding-and-decoding.html)
35. Question about stereo upmixing · Issue #1 · ShanonPearce/ASH-Listening-Set - GitHub, 8月 24, 2025にアクセス、[https://github.com/ShanonPearce/ASH-Listening-Set/issues/1](https://github.com/ShanonPearce/ASH-Listening-Set/issues/1)
36. orchidas/StereoWidener: Plugin to do stereo widening with decorrelation - GitHub, 8月 24, 2025にアクセス、[https://github.com/orchidas/StereoWidener](https://github.com/orchidas/StereoWidener)
37. ckonst/VNDecorrelate: A Velvet-Noise Decorrelator for audio. - GitHub, 8月 24, 2025にアクセス、[https://github.com/ckonst/VNDecorrelate](https://github.com/ckonst/VNDecorrelate)
38. Dynamic Range - Mark Mangini, 8月 24, 2025にアクセス、[https://markmangini.com/Mark_Mangini/Blog/Entries/2024/2/15_Dynamic_Range.html](https://markmangini.com/Mark_Mangini/Blog/Entries/2024/2/15_Dynamic_Range.html)
39. Sound mixing basics | Filmmaking for Journalists Class Notes - Fiveable, 8月 24, 2025にアクセス、[https://library.fiveable.me/filmmaking-for-journalists/unit-4/sound-mixing-basics/study-guide/tYQ5g0UnqCSI1589](https://library.fiveable.me/filmmaking-for-journalists/unit-4/sound-mixing-basics/study-guide/tYQ5g0UnqCSI1589)
40. Dynamic range expander - Simulink - MathWorks, 8月 24, 2025にアクセス、[https://www.mathworks.com/help/audio/ref/expander.html](https://www.mathworks.com/help/audio/ref/expander.html)
41. How to do audio expansion/normalization (emphasise difference between high and low), 8月 24, 2025にアクセス、[https://stackoverflow.com/questions/53259601/how-to-do-audio-expansion-normalization-emphasise-difference-between-high-and-l](https://stackoverflow.com/questions/53259601/how-to-do-audio-expansion-normalization-emphasise-difference-between-high-and-l)
42. Envelope (music) - Wikipedia, 8月 24, 2025にアクセス、[https://en.wikipedia.org/wiki/Envelope_(music)](https://en.wikipedia.org/wiki/Envelope_(music))
43. jmcarlson0320/convolution_reverb - GitHub, 8月 24, 2025にアクセス、[https://github.com/jmcarlson0320/convolution_reverb](https://github.com/jmcarlson0320/convolution_reverb)
44. Convolution Reverb, 8月 24, 2025にアクセス、[https://dvcs.w3.org/hg/audio/raw-file/tip/webaudio/convolution.html](https://dvcs.w3.org/hg/audio/raw-file/tip/webaudio/convolution.html)
45. pyfar.dsp - Read the Docs, 8月 24, 2025にアクセス、[https://pyfar.readthedocs.io/en/latest/modules/pyfar.dsp.html](https://pyfar.readthedocs.io/en/latest/modules/pyfar.dsp.html)
46. Convolution and windowing using a buffer - how do I do overlap add?, 8月 24, 2025にアクセス、[https://dsp.stackexchange.com/questions/29632/convolution-and-windowing-using-a-buffer-how-do-i-do-overlap-add](https://dsp.stackexchange.com/questions/29632/convolution-and-windowing-using-a-buffer-how-do-i-do-overlap-add)
47. vtolani95/convolution - GitHub, 8月 24, 2025にアクセス、[https://github.com/vtolani95/convolution](https://github.com/vtolani95/convolution)
48. Signal Processing (scipy.signal) — SciPy v1.16.1 Manual, 8月 24, 2025にアクセス、[https://docs.scipy.org/doc/scipy/tutorial/signal.html](https://docs.scipy.org/doc/scipy/tutorial/signal.html)
49. How to implement high pass, low pass and bandpass filters in Python's Librosa? - Reddit, 8月 24, 2025にアクセス、[https://www.reddit.com/r/DSP/comments/o75y3d/how_to_implement_high_pass_low_pass_and_bandpass/](https://www.reddit.com/r/DSP/comments/o75y3d/how_to_implement_high_pass_low_pass_and_bandpass/)
50. Parallel Programming with NumPy and SciPy - GeeksforGeeks, 8月 24, 2025にアクセス、[https://www.geeksforgeeks.org/python/parallel-programming-with-numpy-and-scipy/](https://www.geeksforgeeks.org/python/parallel-programming-with-numpy-and-scipy/)
51. spotify/pedalboard: A Python library for audio. - GitHub, 8月 24, 2025にアクセス、[https://github.com/spotify/pedalboard](https://github.com/spotify/pedalboard)
52. librosa.resample — librosa 0.11.0 documentation, 8月 24, 2025にアクセス、[https://librosa.org/doc/main/generated/librosa.resample.html](https://librosa.org/doc/main/generated/librosa.resample.html)
53. Reading a wav file with scipy and librosa in python - Stack Overflow, 8月 24, 2025にアクセス、[https://stackoverflow.com/questions/54482346/reading-a-wav-file-with-scipy-and-librosa-in-python](https://stackoverflow.com/questions/54482346/reading-a-wav-file-with-scipy-and-librosa-in-python)
54. Comparing recurrent convolutional neural networks for large scale bird species classification - PMC, 8月 24, 2025にアクセス、[https://pmc.ncbi.nlm.nih.gov/articles/PMC8385065/](https://pmc.ncbi.nlm.nih.gov/articles/PMC8385065/)
55. Nicholas N Tong, UpmixAl: Automatic Blind Stereo-to-Surround Upmixing Using Music Source Separation Deep Neural Networks - Scholarship@Miami, 8月 24, 2025にアクセス、[https://scholarship.miami.edu/view/pdfCoverPage?instCode=01UOML_INST&filePid=13456422100002976&download=true](https://scholarship.miami.edu/view/pdfCoverPage?instCode=01UOML_INST&filePid=13456422100002976&download=true)
56. Music Source Separation with Hybrid Demucs — Torchaudio 2.8.0 documentation, 8月 24, 2025にアクセス、[https://docs.pytorch.org/audio/master/tutorials/hybrid_demucs_tutorial.html](https://docs.pytorch.org/audio/master/tutorials/hybrid_demucs_tutorial.html)