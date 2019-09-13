# BigCiDian

## 1. Goal
This project is an attempt to create a pronunciation lexicon covering both English and Chinese words *in a unified phoneset* for ASR applications. 

P.S. "CiDian" means "lexicon" in Chinese.

typical use cases in Chinese ASR applications:
``` 
你手机上都装了什么 APP ?
APPLE 的新 MACBOOK PRO 真漂亮
上个月 PRADA 出了款新包包
手机开了 GPRS 导航
世界杯 H 组小组赛
```

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

*notes: If you find anything that doesn't make sense in the mapping table, please let me know, thanks*

### 2.2 Chinese PinYin Mapping
Chinese entries are extracted from [DaCiDian project](https://github.com/aishell-foundation/DaCiDian)

Here is a PinYin to IPA mapping from educational prospective: https://resources.allsetlearning.com/chinese/pronunciation/Pinyin_chart

With a few mapping modifications and symbolic adaptations, here is the final [PinYin to target phoneset mapping](/CN/pinyin_chart.csv)

### 2.3 tone
There are normally 5 tones in Chinese PinYin system ranging from 0 ~ 4.
However there is no tone definition in English.  In BigCiDian, Chinese tonal information is retained and merged with untoned English, so the resulting phoneset may contain 6 tonal variation(1 from English and 5 from Chinese):

```
e.g. for phoneme *ai*

1. HI -> h ai
2. 哎 -> ai_0
3. 掰 -> b ai_1
4. 还 -> h ai_2
5. 凯 -> k ai_3
6. 外 -> w ai_4
```

### 2.4 the unified phoneset
The final unified bi-lingual phoneset details are listed below:

|phoneme|CN example|EN example|
|-|-|-|
|a|把	b a_3| AACHEN	a k ə n|
|æ||CAT	k æ t|
|ai|爱	ai_4| KITE	k ai t|
|an|安	an_1||
|aŋ|羊	y aŋ_2||
|au|老	l au_3| LOUD	l au d|
|b|白	b ai_2| BUT	b ʌ t|
|ch|陈	ch ən_2| CHEST	ch e s t|
|d|大	d a_4| DAY	d ei|
|ð||THIS	ð i s|
|e||BED	b e d|
|ei|累	l ei_4| LAKE	l ei k|
|ə|鹅	ə_2| COCA-COLA	k əu k ə k əu l a|
|ən|陈	ch ən_2||
|əŋ|横	h əŋ_2||
|ər|二	ər_4||
|əu|欧	əu_1|BOAT	b əu t|
|f|房	f aŋ_2|FACE	f ei s|
|g|刚	g aŋ_1|GIVE	g i v|
|h|海	h ai_3|HUG	h ʌ g|
|i|天	t i an_1|HIT	h i t|
|ie|别	b ie_2||
|ii|比	b ii_3|BEAT	b ii t|
|iii|吃	ch iii_1||
|in|音	y in_1||
|iŋ|听	t iŋ_1||
|j|九	j i əu_3||
|k|看	k an_4|CAKE	k ei k|
|l|来	l ai_2|LAKE	l ei k|
|m|马	m a_3|MAKE	m ei k|
|n|那	n a_1|NIKE	n ai k ii|
|ŋ||INTERESTING	i n t ə r e s t i ŋ|
|ɔ||OFF	ɔ f|
|ɔi||JOY	zh ɔi|
|p|胖	p aŋ_4|PACE	p ei s|
|q|钱	q i an_2||
|r|让	ʒ aŋ_4|RISK	r i s k|
|s|丝	s iii_1|SING	s i ŋ|
|sh|上	sh aŋ_4|SHAKE	sh ei k|
|t|团	t u an_2|TIME	t ai m|
|ts|才	ts ai_2||
|u||BOOK	b u k|
|uŋ|从	ts uŋ_2||
|uɔ|桌	zh uɔ_1||
|uu|不	b uu_4|TWO	t uu|
|v||VICTORY	v i k t ə r ii|
|ʌ||CUT	k ʌ t|
|w|王	w aŋ_2|WEST	w e s t|
|x|西	x ii_1||
|y|言	y an_2|YES	y e s|
|yu|去	q yu_4||
|yue|缺	q yue_1||
|z|赞	z an_4|ZOO	z uu|
|zh|中	zh uŋ_1|GESTURE	zh e s ch ə r|
|ʒ|让	ʒ aŋ_4|LEISURE	l e ʒ ə r|
|θ||THINK	θ i ŋ k|

So overall there are 56 phonemes in the unified phoneset(regardless of tones).

Theoretically some phonemes can be split with smaller granularity(eg. au->a u, ɔi->ɔ i, an->a n ...), hence making the phoneset even more compact.  But it is a common practice that larger acoustic modeling units are beneficial for Chinese ASR accuracy, and the existence of decision-tree based state-tying, makes base phoneset size less irrelevant to ASR problem.

I may or may not change the unified phoneset in the future, currently it seems to be sufficient for my purpose.

## 3. Usage
`sh run.sh` should give you a ready-to-use bi-lingual ASR lexicon (`lexicon.txt`), and a phoneset list(`phones.list`) in project root directory.

## 4. Extend entries
To extend the final lexicon with entries of your own interest(say "IPHONE", "华为P30"), you can either:
* add those entries into the very bottom sources(CMUDict and DaCiDian)

or:
* maintain a seperate extension-lexicon, and merge it with main lexicon automatically generated above.

## 5. Experiment result
In [AISHELL-2](https://github.com/kaldi-asr/kaldi/tree/master/egs/aishell2) Mandarin ASR task, replacing Chinese lexicon(DaCiDian) with multilingual CN-EN lexicon(BigCiDian), details are showed below:

For DaCiDian, system performance:
```
----- test -----:
%WER 44.39 [ 21986 / 49532, 338 ins, 2085 del, 19563 sub ] exp/mono/decode_test/cer_9_0.0
%WER 24.25 [ 12011 / 49532, 393 ins, 792 del, 10826 sub ] exp/tri1/decode_test/cer_12_0.0
%WER 22.13 [ 10963 / 49532, 396 ins, 644 del, 9923 sub ] exp/tri2/decode_test/cer_12_0.0
%WER 19.29 [ 9555 / 49532, 263 ins, 640 del, 8652 sub ] exp/tri3/decode_test/cer_13_0.5
%WER 8.33 [ 4125 / 49532, 84 ins, 192 del, 3849 sub ] exp/chain/tdnn_1a/decode_test/cer_8_0.5
```

For BigCiDian, system performance:
```
%WER 43.92 [ 21754 / 49532, 405 ins, 1574 del, 19775 sub ] exp/mono/decode_test/cer_7_0.0
%WER 22.54 [ 11163 / 49532, 406 ins, 652 del, 10105 sub ] exp/tri1/decode_test/cer_11_0.0
%WER 21.09 [ 10445 / 49532, 377 ins, 609 del, 9459 sub ] exp/tri2/decode_test/cer_12_0.0
%WER 18.47 [ 9148 / 49532, 265 ins, 621 del, 8262 sub ] exp/tri3/decode_test/cer_13_0.5
%WER 8.22 [ 4072 / 49532, 68 ins, 260 del, 3744 sub ] exp/chain/tdnn_1a/decode_test/cer_9_0.5
```

__Conclusion__

* It shows that BigCiDian only gives slightly better results than DaCiDian.
* But more importantly, BigCiDian turns a pure Chinese ASR system to multiligual system, which is pretty much the case in nowadays Chinese ASR applications.

THE END