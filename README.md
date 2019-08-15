# BigCiDian

## Goal
This project is an attempt to create a pronunciation lexicon covering both English and Chinese words *in a unified phoneset* for ASR applications.  

P.S. "CiDian" means "lexicon" in Chinese.

## Phoneset
The unified phoneset should be a simple and complementary IPA subset that covers both languages.

### English 
English entries are derived from CMUDict 0.7b, hence we need a mapping from ARPA phoneset to IPA phoneset.

|ARPA|IPA|CMUDict example entries|
|-|-|-|
|AA0 |ɑ|icon:AY1 K AA0 N|
|AA1 |ɑ|heart: HH AA1 R T|
|AA2 |ɑ|kmart: K EY1 M AA2 R T|
|AE0 |æ|romance: R OW1 M AE0 N S|
|AE1 |æ|lambda: L AE1 M D AH0|
|AE2 |æ|setback: S EH1 T B AE2 K|
|AH0 |ə|station: S T EY1 SH AH0 N|
|AH1 |ʌ|bug: B AH1 G|
|AH2 |ʌ|haircut: HH EH1 R K AH2 T|
|AO0 |ɔ|hongkong: HH AO1 NG K AO0 NG|
|AO1 |ɔ|law: L AO1|
|AO2 |ɔ|layoff: L EY1 AO2 F|
|AW0 |aʊ|foundation: F AW0 N D EY1 SH AH0 N|
|AW1 |aʊ|founder: F AW1 N D ER0|
|AW2 |aʊ|hometown: HH OW1 M T AW2 N|
|AY0 |aɪ|hypothese: HH AY0 P AA1 TH AH0 S IY2 Z|
|AY1 |aɪ|ice: AY1 S|
|AY2 |aɪ|iceland: AY1 S L AH0 N D|
|B |b|bike: B AY1 K|
|CH |tʃ|chase: CH EY1 S|
|D |d|desk: D EH1 S K|
|DH |ð|those: DH OW1 Z|
|EH0 |e|princess: P R IH1 N S EH0 S|
|EH1 |e|professor: P R AH0 F EH1 S ER0|
|EH2 |e|progress: P R AA1 G R EH2 S|
|ER0 |ə r|programmer: P R OW1 G R AE2 M ER0|
|ER1 |ə r|purge: P ER1 JH|
|ER2 |ə r|showgirl: SH OW1 G ER2 L|
|EY0 |eɪ|eighteen: EY0 T IY1 N|
|EY1 |eɪ|email: IY0 M EY1 L|
|EY2 |eɪ|thursday: TH ER1 Z D EY2|
|F |f|face: F EY1 S|
|G |g|give: G IH1 V|
|HH |h|hey: HH EY1|
|IH0 |ɪ|facing: F EY1 S IH0 NG |
|IH1 |ɪ|fear: F IH1 R|
|IH2 |ɪ|fellowship: F EH1 L OW0 SH IH2 P|
|IY0 |i|lady: L EY1 D IY0|
|IY1 |i|prefix: P R IY1 F IH0 K S|
|IY2 |i|kenny: K EH1 N IY2|
|JH |dʒ|gesture: JH EH1 S CH ER0|
|K |k|cat: K AE1 T|
|L |l|lack: L AE1 K|
|M |m|may: M EY1|
|N |n|no: N OW1|
|NG |ŋ|thing: TH IH1 NG|
|OW0 |əʊ|crypto: K R IH1 P T OW0|
|OW1 |əʊ|token: T OW1 K AH0 N|
|OW2 |əʊ|earphone: IH1 R F OW2 N|
|OY0 |ɔɪ|invoice: IH1 N V OY0 S|
|OY1 |ɔɪ|floyd: F L OY1 D|
|OY2 |ɔɪ|episode: EH1 P IH0 S OW2 D|
|P |p|pat: P AE1 T|
|R |r|risk: R IH1 S K|
|S |s|sing: S IH1 NG|
|SH |ʃ|shake: SH EY1 K|
|T |t|test: T EH1 S T|
|TH |θ|think: TH IH1 NG K|
|UH0 |ʊ|fulfill: F UH0 L F IH1 L|
|UH1 |ʊ|full: F UH1 L|
|UH2 |ʊ|goodbye: G UH2 D B AY1|
|UW0 |u|rescue: R EH1 S K Y UW0|
|UW1 |u|refuse: R AH0 F Y UW1 Z|
|UW2 |u|restroom: R EH1 S T R UW2 M|
|V |v|very: V EH1 R IY0|
|W |w|west: W EH1 S T|
|Y |y|yes: Y EH1 S|
|Z |z|zero: Z IY1 R OW0|
|ZH |ʒ|illusion: IH2 L UW1 ZH AH0 N|

*notes: If you find anything inappropriate in the mapping, please open an issue and help me improve it, thanks*


### Chinese
Chinese entries are extracted from DaCiDian project that primarily deals with Chinese words.
