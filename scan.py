import sys, pprint
from collections  import Counter
import GenWordsFromFiles as wg

dirname = r'./Texts' if len(sys.argv) == 1 else sys.argv[1]

words = wg.gen_words(dirname)
c = Counter(words)

print(' Words: ','-'*20)
print(words[:90])
print('-'*30)

print(c.most_common()[:-60:-1])
pprint.pprint(c.most_common(30))
