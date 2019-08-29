import os, sys, codecs, re

mapf = sys.argv[1]
arpaf = sys.argv[2]
ipaf = sys.argv[3]

m = {}

for l in codecs.open(mapf, 'r', 'utf8'):
    cols = l.strip().split()
    m[cols[0]] = u' '.join(cols[1:])

ipa = codecs.open(ipaf, 'w+', 'utf8')

for l in codecs.open(arpaf, 'r', 'utf8'):
    if ';;;' in l:
        continue
    cols = l.strip().split()
    word = cols[0]
    word = re.sub('\([0-9]*\)','',word)
    pron = cols[1:]
    ipa_pron = [ m[phn] for phn in pron ]
    ipa.write(word + u'\t' + u' '.join(ipa_pron) + u'\n')

ipa.close()
