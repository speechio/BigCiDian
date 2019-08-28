# coding=utf8
import codecs, sys

fi = codecs.open(sys.argv[1], 'r', 'utf8')
fo = codecs.open(sys.argv[2], 'w+', 'utf8')

m = {}

for l in fi:
    cols = l.strip().split(',')
    for col in cols:
        if '[' in col:
            pinyin = col.split('[')[0].strip()
            phones = col.split('[')[1].strip().strip(']')
            m[pinyin] = phones

for k in sorted(m.keys()):
    fo.write(u'{}\t{}\n'.format(k, m[k]))

fi.close()
fo.close()
