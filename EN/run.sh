iconv -f ISO_8859-10 -t utf8 cmudict-0.7b > tmp # convert raw format from IOS-8859 to UTF8
#python ../utils/dict_to_phoneset.py tmp ARPA.list
python ../utils/map.py ARPA2IPA.map tmp EN.txt
rm tmp
