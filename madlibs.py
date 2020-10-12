import re, os, sys

def mad_lib(file_name: str):
    adjective_reg = re.compile('ADJECTIVE')
    noun_reg = re.compile('NOUN')
    verb_reg = re.compile('VERB')
    re_S = re.compile(r'(\S+)')

    if os.path.exists(file_name):
        file = open(file_name, 'r+')
        text = file.read()
        word_list = re_S.split(text)

        for i in range(len(word_list)):
            if adjective_reg.search(word_list[i]):
                word_list[i] = input('give me adjective:')
            if noun_reg.search(word_list[i]):
                word_list[i] = input('give me noun:')
            if verb_reg.search(word_list[i]):
                word_list[i] = input('give me verb:')
        text = ''.join(word_list)
        file.seek(0)
        file.truncate()
        file.write(text)
        print(text)
    print('thank you for your attention')
    sys.exit()

mad_lib('some_text.txt')
        

        




