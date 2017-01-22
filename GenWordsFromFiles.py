import os, re
import cchardet as chardet

#spliter = re.compile("((?:[a-zA-Z]+[-']?)*[a-zA-Z]+)")   ##r'\w+')
spliter = re.compile(r'\w+')
def gen_wordslist(line):
    yield spliter.findall(line.lower())
    ##yield line.split()

def detect_encoding(fullname):
    with open(fullname, 'rb') as data:
        result = chardet.detect(data.read())
    return result['encoding']

encodings = ['windows-1251', 'utf-8', 'cp866', 'KOI8-R']
def detect_encoding_fast(fullname):
    for e in encodings:
        try:
            with open(fullname, encoding=e) as data:
                data.readlines()
        except UnicodeDecodeError:
            print('got unicode error with %s , trying different encoding' % e)
        else:
            print('opening the file with encoding:  %s ' % e)
            break

    
def gen_lines(fullname):
    encoding = detect_encoding(fullname)
    ##if encoding == 'MAC-CYRILLIC' : encoding = 'windows-1251'
    print(fullname, encoding)
    with open(fullname, encoding=encoding) as data:    #, encoding='MAC-CYRILLIC' cp866
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
    dirname = os.path.abspath(dirname)
    for (thisDir, subsHere, filesHere) in os.walk(dirname, followlinks=True):
        print(filesHere)
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
'''

if __name__ == "__main__":
    import sys, pprint, pickle
    from collections  import Counter

    try:
        with open('data_.pickle', 'rb') as f:
            words = pickle.load(f)
    except:
        readed_pickle = False
        dirname = r'../Txt' if len(sys.argv) == 1 else sys.argv[1]
        words = gen_words(dirname)
    else:
        readed_pickle = True


    c = Counter(words)
    print(c.most_common()[:-50:-1])
    pprint.pprint(c.most_common(25))

    if readed_pickle == False:
        with open('data.pickle', 'wb') as f:
            pickle.dump(words, f)
