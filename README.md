# BigCiDian

## 1. Goal
This project is an attempt to create a pronunciation lexicon covering both English and Chinese words *in a unified phoneset* for ASR applications.  

P.S. "CiDian" means "lexicon" in Chinese.

## 2. Phoneset
The unified phoneset should be a simple and complementary IPA subset that covers both languages.

### 2.1 English Phoneset Mapping
English entries are derived from CMUDict 0.7b, hence we need a mapping from ARPA phoneset to IPA phoneset.

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

The actual mapping is developed from this source: https://resources.allsetlearning.com/chinese/pronunciation/Pinyin_chart


|Initial-/-Final|-a        |-ai         |-ao         |-an         |-ang         |-e        |-ei         |-en         |-eng         |-er     |-o        |-ou         |-ong         |-i       |-i*         |-ia        |-iao         |-ie       |-iu         |-ian         |-iang         |-in       |-ing       |-iong         |-u         |-ua          |-uai           |-ui           |-uo          |-uan           |-uang           |-un           |-ü       |-üe        |-üan          |-ün         |
|------|----------|------------|------------|------------|-------------|----------|------------|------------|-------------|--------|----------|------------|-------------|---------|------------|-----------|-------------|----------|------------|-------------|--------------|----------|-----------|--------------|-----------|-------------|---------------|--------------|-------------|---------------|----------------|--------------|---------|-----------|--------------|------------|
|∅-    |a [a]     |ai [ai]     |ao [au]     |an [an]     |ang [aŋ]     |e [ə]     |ei [ei]     |en [ən]     |eng [əŋ]     |er [ə r]|o [ɔ]     |ou [əu]     |             |         |            |           |             |          |            |             |              |          |           |              |           |             |               |              |             |               |                |              |         |           |              |            |
|b-    |ba [b a]  |bai [b ai]  |bao [b au]  |ban [b an]  |bang [b aŋ]  |          |bei [b ei]  |ben [b ən]  |beng [b əŋ]  |        |bo [b u ɔ]|            |             |bi [b ii]|            |           |biao [b i au]|bie [b ie]|            |bian [b i an]|              |bin [b in]|bing [b iŋ]|              |bu [b uu]  |             |               |              |             |               |                |              |         |           |              |            |
|c-    |ca [ts a] |cai [ts ai] |cao [ts au] |can [ts an] |cang [ts aŋ] |ce [ts ə] |cei [ts ei] |cen [ts ən] |ceng [ts əŋ] |        |          |cou [ts əu] |cong [ts uŋ] |         |ci [ts iii] |           |             |          |            |             |              |          |           |              |cu [ts uu] |             |               |cui [ts u ei] |cuo [ts u ɔ] |cuan [ts u an] |                |cun [ts u ən] |         |           |              |            |
|ch-   |cha [ch a]|chai [ch ai]|chao [ch au]|chan [ch an]|chang [ch aŋ]|che [ch ə]|            |chen [ch ən]|cheng [ch əŋ]|        |          |chou [ch əu]|chong [ch uŋ]|         |chi [ch iii]|           |             |          |            |             |              |          |           |              |chu [ch uu]|chua [ch u a]|chuai [ch u ai]|chui [ch u ei]|chuo [ch u ɔ]|chuan [ch u an]|chuang [ch u aŋ]|chun [ch u ən]|         |           |              |            |
|d-    |da [d a]  |dai [d ai]  |dao [d au]  |dan [d an]  |dang [d aŋ]  |de [d ə]  |dei [d ei]  |den [d ən]  |deng [d əŋ]  |        |          |dou [d əu]  |dong [d uŋ]  |di [d ii]|            |           |diao [d i au]|die [d ie]|diu [d i əu]|dian [d i an]|              |          |ding [d iŋ]|              |du [d uu]  |             |               |dui [d u ei]  |duo [d u ɔ]  |duan [d u an]  |                |dun [d u ən]  |         |           |              |            |
|f-    |fa [f a]  |            |            |fan [f an]  |fang [f aŋ]  |          |fei [f ei]  |fen [f ən]  |feng [f əŋ]  |        |fo [f u ɔ]|fou [f əu]  |             |         |            |           |             |          |            |             |              |          |           |              |fu [f uu]  |             |               |              |             |               |                |              |         |           |              |            |
|g-    |ga [g a]  |gai [g ai]  |gao [g au]  |gan [g an]  |gang [g aŋ]  |ge [g ə]  |gei [g ei]  |gen [g ən]  |geng [g əŋ]  |        |          |gou [g əu]  |gong [g uŋ]  |         |            |           |             |          |            |             |              |          |           |              |gu [g uu]  |gua [g u a]  |guai [g u ai]  |gui [g u ei]  |guo [g u ɔ]  |guan [g u an]  |guang [g u aŋ]  |gun [g u ən]  |         |           |              |            |
|h-    |ha [h a]  |hai [h ai]  |hao [h au]  |han [h an]  |hang [h aŋ]  |he [h ə]  |hei [h ei]  |hen [h ən]  |heng [h əŋ]  |        |          |hou [h əu]  |hong [h uŋ]  |         |            |           |             |          |            |             |              |          |           |              |hu [h uu]  |hua [h u a]  |huai [h u ai]  |hui [h u ei]  |huo [h u ɔ]  |huan [h u an]  |huang [h u aŋ]  |hun [h u ən]  |         |           |              |            |
|j-    |          |            |            |            |             |          |            |            |             |        |          |            |             |ji [j ii]|            |jia [j i a]|jiao [j i au]|jie [j ie]|jiu [j i əu]|jian [j i an]|jiang [j i aŋ]|jin [j in]|jing [j iŋ]|jiong [j i uŋ]|           |             |               |              |             |               |                |              |jv [j yu]|jve [j yue]|jvan [j yu an]|jvn [j yu n]|
|k-    |ka [k a]  |kai [k ai]  |kao [k au]  |kan [k an]  |kang [k aŋ]  |ke [k ə]  |kei [k ei]  |ken [k ən]  |keng [k əŋ]  |        |          |kou [k əu]  |kong [k uŋ]  |         |            |           |             |          |            |             |              |          |           |              |ku [k uu]  |kua [k u a]  |kuai [k u ai]  |kui [k u ei]  |kuo [k u ɔ]  |kuan [k u an]  |kuang [k u aŋ]  |kun [k u ən]  |         |           |              |            |
|l-    |la [l a]  |lai [l ai]  |lao [l au]  |lan [l an]  |lang [l aŋ]  |le [l ə]  |lei [l ei]  |            |leng [l əŋ]  |        |lo [l u ɔ]|lou [l əu]  |long [l uŋ]  |li [l ii]|            |lia [l i a]|liao [l i au]|lie [l ie]|liu [l i əu]|lian [l i an]|liang [l i aŋ]|lin [l in]|ling [l iŋ]|              |lu [l uu]  |             |               |              |luo [l u ɔ]  |luan [l u an]  |                |lun [l u ən]  |lv [l yu]|lve [l yue]|              |            |
|m-    |ma [m a]  |mai [m ai]  |mao [m au]  |man [m an]  |mang [m aŋ]  |me [m ə]  |mei [m ei]  |men [m ən]  |meng [m əŋ]  |        |mo [m u ɔ]|mou [m əu]  |             |mi [m ii]|            |           |miao [m i au]|mie [m ie]|miu [m i əu]|mian [m i an]|              |min [m in]|ming [m iŋ]|              |mu [m uu]  |             |               |              |             |               |                |              |         |           |              |            |
|n-    |na [n a]  |nai [n ai]  |nao [n au]  |nan [n an]  |nang [n aŋ]  |ne [n ə]  |nei [n ei]  |nen [n ən]  |neng [n əŋ]  |        |          |nou [n əu]  |nong [n uŋ]  |ni [n ii]|            |           |niao [n i au]|nie [n ie]|niu [n i əu]|nian [n i an]|niang [n i aŋ]|nin [n in]|ning [n iŋ]|              |nu [n uu]  |             |               |              |nuo [n u ɔ]  |nuan [n u an]  |                |              |nv [n yu]|nve [n yue]|              |            |
|p-    |pa [p a]  |pai [p ai]  |pao [p au]  |pan [p an]  |pang [p aŋ]  |          |pei [p ei]  |pen [p ən]  |peng [p əŋ]  |        |po [p u ɔ]|pou [p əu]  |             |pi [p ii]|            |           |piao [p i au]|pie [p ie]|            |pian [p i an]|              |pin [p in]|ping [p iŋ]|              |pu [p uu]  |             |               |              |             |               |                |              |         |           |              |            |
|q-    |          |            |            |            |             |          |            |            |             |        |          |            |             |qi [q ii]|            |qia [q i a]|qiao [q i au]|qie [q ie]|qiu [q i əu]|qian [q i an]|qiang [q i aŋ]|qin [q in]|qing [q iŋ]|qiong [q i uŋ]|           |             |               |              |             |               |                |              |qv [q yu]|qve [q yue]|qvan [q yu an]|qvn [q yu n]|
|r-    |          |            |rao [ʒ au]  |ran [ʒ an]  |rang [ʒ aŋ]  |re [ʒ ə]  |            |ren [ʒ ən]  |reng [ʒ əŋ]  |        |          |rou [ʒ əu]  |rong [ʒ uŋ]  |         |ri [ʒ iii]  |           |             |          |            |             |              |          |           |              |ru [ʒ uu]  |rua [ʒ u a]  |               |rui [ʒ u ei]  |ruo [ʒ u ɔ]  |ruan [ʒ u an]  |                |run [ʒ u ən]  |         |           |              |            |
|s-    |sa [s a]  |sai [s ai]  |sao [s au]  |san [s an]  |sang [s aŋ]  |se [s ə]  |            |sen [s ən]  |seng [s əŋ]  |        |          |sou [s əu]  |song [s uŋ]  |         |si [s iii]  |           |             |          |            |             |              |          |           |              |su [s uu]  |             |               |sui [s u ei]  |suo [s u ɔ]  |suan [s u an]  |                |sun [s u ən]  |         |           |              |            |
|sh-   |sha [sh a]|shai [sh ai]|shao [sh au]|shan [sh an]|shang [sh aŋ]|she [sh ə]|shei [sh ei]|shen [sh ən]|sheng [sh əŋ]|        |          |shou [sh əu]|             |         |shi [sh iii]|           |             |          |            |             |              |          |           |              |shu [sh uu]|shua [sh u a]|shuai [sh u ai]|shui [sh u ei]|shuo [sh u ɔ]|shuan [sh u an]|shuang [sh u aŋ]|shun [sh u ən]|         |           |              |            |
|t-    |ta [t a]  |tai [t ai]  |tao [t au]  |tan [t an]  |tang [t aŋ]  |te [t ə]  |            |            |teng [t əŋ]  |        |          |tou [t əu]  |tong [t uŋ]  |ti [t ii]|            |           |tiao [t i au]|tie [t ie]|            |tian [t i an]|              |          |ting [t iŋ]|              |tu [t uu]  |             |               |tui [t u ei]  |tuo [t u ɔ]  |tuan [t u an]  |                |tun [t u ən]  |         |           |              |            |
|w-    |wa [w ɑ]  |wai [w aɪ]  |            |wan [w an]  |wang [w aŋ]  |          |wei [w ei]  |wen [w ən]  |weng [w əŋ]  |        |wo [w ɔ]  |            |             |         |            |           |             |          |            |             |              |          |           |              |wu [w uu]  |             |               |              |             |               |                |              |         |           |              |            |
|x-    |          |            |            |            |             |          |            |            |             |        |          |            |             |xi [x ii]|            |xia [x i a]|xiao [x i au]|xie [x ie]|xiu [x i əu]|xian [x i an]|xiang [x i aŋ]|xin [x in]|xing [x iŋ]|xiong [x i uŋ]|           |             |               |              |             |               |                |              |xv [x yu]|xve [x yue]|xvan [x yu an]|xvn [x yu n]|
|y-    |ya [y a]  |            |yao [y au]  |yan [y an]  |yang [y aŋ]  |ye [y ie] |            |            |             |        |          |you [y əu̯] |yong [y uŋ]  |yi [y ii]|            |           |             |          |            |             |              |yin [y in]|ying [y iŋ]|              |           |             |               |              |             |               |                |              |yv [yu]  |yve [yue]  |yvan [yu an]  |yvn [yu n]  |
|z-    |za [z a]  |zai [z ai]  |zao [z au]  |zan [z an]  |zang [z aŋ]  |ze [z ə]  |zei [z ei]  |zen [z ən]  |zeng [z əŋ]  |        |          |zou [z əu]  |zong [z uŋ]  |         |zi [z iii]  |           |             |          |            |             |              |          |           |              |zu [z uu]  |             |               |zui [z u ei]  |zuo [z u ɔ]  |zuan [z u an]  |                |zun [z u ən]  |         |           |              |            |
|zh-   |zha [zh a]|zhai [zh ai]|zhao [zh au]|zhan [zh an]|zhang [zh aŋ]|zhe [zh ə]|zhei [zh ei]|zhen [zh ən]|zheng [zh əŋ]|        |          |zhou [zh əu]|zhong [zh uŋ]|         |zhi [zh iii]|           |             |          |            |             |              |          |           |              |zhu [zh uu]|zhua [zh u a]|zhuai [zh u ai]|zhui [zh u ei]|zhuo [zh u ɔ]|zhuan [zh u an]|zhuang [zh u aŋ]|zhun [zh u ən]|         |           |              |            |
