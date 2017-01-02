import sys, os, pprint

trace = 0 # 1=каталоги, 2=+файлы
dirname = r'./Texts' if len(sys.argv) == 1 else sys.argv[1]

allsizes = []
for (thisDir, subsHere, filesHere) in os.walk(dirname, followlinks=True):
    if trace: print(thisDir)
    for filename in filesHere:
        if filename.endswith(('.txt','.srt')):    ## or filename.endswith('.srt'):
            if trace > 1: print('...', filename)
            fullname = os.path.join(thisDir, filename)
            try:
                txtsize = os.path.getsize(fullname)
            except os.error:
                print('skipping', fullname, sys.exc_info()[0])
            else:
                lines = len(open(fullname, 'rb').readlines())
                allsizes.append((txtsize, lines, filename))
allsizes.sort()
pprint.pprint(allsizes[:3])
pprint.pprint(allsizes[-3:])



