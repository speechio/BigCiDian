# BigCiDian

## 1. Goal
This project is an attempt to create a pronunciation lexicon covering both English and Chinese words *in a unified phoneset* for ASR applications.  

P.S. "CiDian" means "lexicon" in Chinese.

## 2. Phoneset
The unified phoneset should be a simple and precise phoneset that covers both languages. Note that the mapping listed below are heavily based on IPA.

### 2.1 English Phoneset Mapping
English entries are derived from CMUDict 0.7b, hence we need a mapping from ARPA phoneset to target phoneset.

|ARPA|IPA|CMUDict example entries|
|-|-|-|
|AA0 |a|icon:AY1 K AA0 N|
|AA1 |a|heart: HH AA1 R T|
|AA2 |a|kmart: K EY1 M AA2 R T|
|AE0 |æ|romance: R OW1 M AE0 N S|
|AE1 |æ|lambda: L AE1 M D AH0|
|AE2 |æ|setback: S EH1 T B AE2 K|
|AH0 |ə|station: S T EY1 SH AH0 N|
|AH1 |ʌ|bug: B AH1 G|
|AH2 |ʌ|haircut: HH EH1 R K AH2 T|
|AO0 |ɔ|hongkong: HH AO1 NG K AO0 NG|
|AO1 |ɔ|law: L AO1|
|AO2 |ɔ|layoff: L EY1 AO2 F|
|AW0 |au|foundation: F AW0 N D EY1 SH AH0 N|
|AW1 |au|founder: F AW1 N D ER0|
|AW2 |au|hometown: HH OW1 M T AW2 N|
|AY0 |ai|hypothese: HH AY0 P AA1 TH AH0 S IY2 Z|
|AY1 |ai|ice: AY1 S|
|AY2 |ai|iceland: AY1 S L AH0 N D|
|B |b|bike: B AY1 K|
|CH |ch|chase: CH EY1 S|
|D |d|desk: D EH1 S K|
|DH |ð|those: DH OW1 Z|
|EH0 |e|princess: P R IH1 N S EH0 S|
|EH1 |e|professor: P R AH0 F EH1 S ER0|
|EH2 |e|progress: P R AA1 G R EH2 S|
|ER0 |ə r|programmer: P R OW1 G R AE2 M ER0|
|ER1 |ə r|purge: P ER1 JH|
|ER2 |ə r|showgirl: SH OW1 G ER2 L|
|EY0 |ei|eighteen: EY0 T IY1 N|
|EY1 |ei|email: IY0 M EY1 L|
|EY2 |ei|thursday: TH ER1 Z D EY2|
|F |f|face: F EY1 S|
|G |g|give: G IH1 V|
|HH |h|hey: HH EY1|
|IH0 |i|facing: F EY1 S IH0 NG |
|IH1 |i|fear: F IH1 R|
|IH2 |i|fellowship: F EH1 L OW0 SH IH2 P|
|IY0 |ii|email: IY0 M EY1 L|
|IY1 |ii|prefix: P R IY1 F IH0 K S|
|IY2 |ii|increase: IH1 N K R IY2 S|
|JH |zh|gesture: JH EH1 S CH ER0|
|K |k|cat: K AE1 T|
|L |l|lack: L AE1 K|
|M |m|may: M EY1|
|N |n|no: N OW1|
|NG |ŋ|thing: TH IH1 NG|
|OW0 |əu|crypto: K R IH1 P T OW0|
|OW1 |əu|token: T OW1 K AH0 N|
|OW2 |əu|earphone: IH1 R F OW2 N|
|OY0 |ɔi|invoice: IH1 N V OY0 S|
|OY1 |ɔi|floyd: F L OY1 D|
|OY2 |ɔi|episode: EH1 P IH0 S OW2 D|
|P |p|pat: P AE1 T|
|R |r|risk: R IH1 S K|
|S |s|sing: S IH1 NG|
|SH |sh|shake: SH EY1 K|
|T |t|test: T EH1 S T|
|TH |θ|think: TH IH1 NG K|
|UH0 |u|fulfill: F UH0 L F IH1 L|
|UH1 |u|full: F UH1 L|
|UH2 |u|goodbye: G UH2 D B AY1|
|UW0 |uu|rescue: R EH1 S K Y UW0|
|UW1 |uu|fool: F UW1 L|
|UW2 |uu|restroom: R EH1 S T R UW2 M|
|V |v|very: V EH1 R IY0|
|W |w|west: W EH1 S T|
|Y |y|yes: Y EH1 S|
|Z |z|zero: Z IY1 R OW0|
|ZH |ʒ|illusion: IH2 L UW1 ZH AH0 N|

*notes: If you find anything inappropriate in the mapping, please open an issue and help me improve it, thanks*

### 2.2 Chinese PinYin Mapping
Chinese entries are extracted from DaCiDian project that primarily deals with Chinese words.

Here is a PinYin to IPA mapping in educational prospective: https://resources.allsetlearning.com/chinese/pronunciation/Pinyin_chart

With a few mapping modifications and symbolic adaptations, here is [the final PinYin to target phoneset mapping](/CN/pinyin_mapping_chart.csv)

### 2.3 the unified phoneset
TBC