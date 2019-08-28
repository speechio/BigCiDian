python ../utils/convert_pinyin_chart_to_mapping.py pinyin_chart.csv pinyin_to_phone.txt
python ../utils/DaCiDian.py word_to_pinyin.txt pinyin_to_phone.txt > CN.txt
