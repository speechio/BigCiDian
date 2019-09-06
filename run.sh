cd EN/
sh run.sh
cd -

cd CN/
sh run.sh
cd -

#cat EN/EN.txt CN/CN.txt | sort -k1 -d > lexicon.txt
#cat EN/EN.txt CN/CN.txt | sort -k1 > lexicon.txt
cat EN/EN.txt CN/CN.txt | sort -u > lexicon.txt
rm EN/EN.txt CN/CN.txt

python utils/dict_to_phoneset.py lexicon.txt phoneset.list
