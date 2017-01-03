import sys, os, pprint, re

dirname = r'./Texts' if len(sys.argv) == 1 else sys.argv[1]

def gen_lines(fullname):
    with open(fullname) as data:  # open(file, encoding="cp866")
        for line in data:
            line = line.strip() # TODO: Убрать!
            if len(line) > 0:
                yield line
            '''TODO: Склеивать в абзац, определять пунктуацию'''


def gen_filelist():
    for (thisDir, subsHere, filesHere) in os.walk(dirname, followlinks=True):
        for filename in filesHere:
            if filename.endswith(('.txt','.srt')):
                fullname = os.path.join(thisDir, filename)
                yield fullname
                                           

allsizes = []
lines = []

for fname in gen_filelist():
    print(fname)
    for line in gen_lines(fname):
        lines.append(line)

pprint.pprint(lines[:15])
