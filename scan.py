import sys, os, pprint

trace = 0
dirname = r'./Texts' if len(sys.argv) == 1 else sys.argv[1]

allsizes = []
for (thisDir, subsHere, filesHere) in os.walk(dirname, followlinks=True):
    if trace: print(thisDir)
    for filename in filesHere:
        if filename.endswith('.txt'):
            if trace: print('...', filename)
            fullname = os.path.join(thisDir, filename)
            fullsize = os.path.getsize(fullname)
            allsizes.append((fullsize, fullname))
allsizes.sort()
pprint.pprint(allsizes[:2])
pprint.pprint(allsizes[-2:])



