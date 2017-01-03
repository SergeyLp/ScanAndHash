import os, re

spliter = re.compile("((?:[a-zA-Z]+[-']?)*[a-zA-Z]+)")   ##r'\w+')

def gen_wordslist(line):
    yield spliter.findall(line.lower())
    ##yield line.split()


def gen_lines(fullname):
    with open(fullname) as data:    #, encoding="cp866"
        if fullname.endswith('.srt'):
            numLineInBlock = 0
            for line in data:
                if len(line) == 1:
                    numLineInBlock = 0
                    continue
                numLineInBlock += 1
                if numLineInBlock < 3:
                    continue
                yield line.strip()
        else:
            for line in data:
                line = line.strip() # TODO: Убрать!
                if len(line) > 0:
                    yield line


def gen_filelist(dirname):
    for (thisDir, subsHere, filesHere) in os.walk(dirname, followlinks=True):
        for filename in filesHere:
            if filename.endswith(('.txt','.srt')):
                fullname = os.path.join(thisDir, filename)
                yield fullname


def gen_words(dirname):
    words = []
    for fname in gen_filelist(dirname):
        for line in gen_lines(fname):
            for wordlist in gen_wordslist(line):
                ##words.append(word)
                words += wordlist
    return words            


'''
TODO: Склеивать в абзац, определять пунктуацию
Reading varias coding of text
'''

if __name__ == "__main__":
    import sys, pprint
    from collections  import Counter
    
    dirname = r'./Texts' if len(sys.argv) == 1 else sys.argv[1]

    words = gen_words(dirname)
    c = Counter(words)


    print(c.most_common()[:-60:-1])
    pprint.pprint(c.most_common(30))
