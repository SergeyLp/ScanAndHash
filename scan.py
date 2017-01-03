import sys, os, pprint, re

dirname = r'./Texts' if len(sys.argv) == 1 else sys.argv[1]

def gen_wordslist(line: str):    
    yield line.split()


def gen_lines(fullname):
    with open(fullname) as data:  # open(file, encoding="cp866")
        for line in data:
            line = line.strip() # TODO: Убрать!
            if len(line) > 0:
                yield line


def gen_filelist():
    for (thisDir, subsHere, filesHere) in os.walk(dirname, followlinks=True):
        for filename in filesHere:
            if filename.endswith(('.txt','.srt')):
                fullname = os.path.join(thisDir, filename)
                yield fullname


words = []

for fname in gen_filelist():
    for line in gen_lines(fname):
        for wordlist in gen_wordslist(line):
            ##words.append(word)
            #words += word
            words = [*words, *wordlist]

print(words[:40])
pprint.pprint(words[:13])
'''
TODO: Склеивать в абзац, определять пунктуацию
Reading varias coding of text
'''
