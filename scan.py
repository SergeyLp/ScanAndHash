import sys, pprint
from GenWordsFromFiles import *  ## as wg

dirname = r'./Texts' if len(sys.argv) == 1 else sys.argv[1]

##words = []
words = gen_words(dirname)

print(words[:60])
pprint.pprint(words[:13])
