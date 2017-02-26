import sys, pprint, pickle, zlib
from collections  import Counter
import timeit
import time
import farmhash, mmh3

import GenWordsFromFiles as wg

with open('all_word_set.pickle', 'rb') as f:
    ws = pickle.load(f)

by_hashes = {}
collusions  = []

start = time.time()
for w in ws:
        ##h = str.__hash__(w)
        h = farmhash.fingerprint32(w)
        if h in by_hashes: collusions.append((h, by_hashes[h], w))
        by_hashes[h] = w
end = time.time()
print('Time:', end-start)

print('Collusions:', len(collusions))
pprint.pprint(collusions[:10])

