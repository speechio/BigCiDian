cd EN/
sh run.sh
cd -

cd CN/
sh run.sh
cd -

#cat EN/EN.txt CN/CN.txt | sort -d -k1 > lexicon.txt
cat EN/EN.txt CN/CN.txt | sort -k1 > lexicon.txt
rm EN/EN.txt CN/CN.txt

python utils/dict2phoneset.py lexicon.txt phones.txt
