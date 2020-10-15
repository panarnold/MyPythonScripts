#! python
# fillTheGap.py - script responsible for finding files which specific prefix (e.g. 'spam004', 'spam007')
# and filling the gap beetwen them - for example, if u got spam_004 file and next file has the
# spam_006 name, it will change it accordingly into spam_001 and spam_002
# X 2020 Arnold Cytrowski

import os, re, shutil, sys

def find_files():
    filelist = []
    current_prefix = re.compile(input('put your prefix here buddy:\n'))
    

    for folder, subfolders, filenames in os.walk('.'):
        for filename in filenames:
            if current_prefix.search(filename) is not None:
                filepath = os.path.join(folder, filename)
                print(f'found {filepath}')
                filelist.append(filepath)

    print(filelist)
    return filelist

def renamer():
    filelist = find_files()
    newlist= []
    num_prefix = re.compile(r'[1-9]+0*[1-9]*0{,1}?')

    index = 1
    for filename in filelist:

        if num_prefix.search(filename) is not None:
            new_filename = num_prefix.sub(str(index), filename)
            print(f'changing {filename} to {new_filename}')
            shutil.move(filename, new_filename)
            index += 1
    
    print('ok my job here is done')
    sys.exit()
    




renamer()
