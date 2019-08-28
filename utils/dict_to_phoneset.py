# -*- encoding: utf8

import sys, os
import codecs

dict_filename = sys.argv[1]
phoneset_filename = sys.argv[2]

phoneset = []

fi = codecs.open(dict_filename, 'r', 'utf8')

for l in fi.readlines():
    if ';;;' in l:
        continue
    cols = l.strip().split()
    word = cols[0]
    phones = cols[1:]
    for p in phones:
        if p not in phoneset:
            phoneset.append(p)

fi.close()

fo = codecs.open(phoneset_filename, 'w+', 'utf8')
for phone in sorted(phoneset):
    fo.write(phone + '\n')
fo.close()
