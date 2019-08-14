iconv -f ISO_8859-10 -t utf8 cmudict-0.7b > tmp # convert raw format from IOS-8859 to UTF8
python ../utils/dict2phoneset.py tmp ARPA.list
python ../utils/map.py ARPA2IPA.map tmp cmudict-0.7b_ipa
rm tmp
