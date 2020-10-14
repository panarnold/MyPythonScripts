#! python
# this script will ask you for size of file which you want to detect and print in on the console
# X 2020 Arnold Cytrowski

import os, enum, send2trash, re, sys

class SIZE_UNIT(enum.Enum):
    BYTES = 'BYTES'
    KB = 'KB'
    MB = 'MB'
    GB = 'GB'



def input_value():
    return (input('ok boy, 1step: give me the size and the unit(BYTES/KB/MB/GB)):\n'))

def spliter(input: str):
    num_reg = re.compile(r'\d+')
    lit_reg = re.compile(r'[^\d\s]+')
    mo_n = num_reg.search(input)
    mo_l = lit_reg.search(input)
    if mo_n is not None and mo_l is not None:
        if(mo_n.group().isnumeric() and mo_l.group().isalpha()):
            print(mo_n.group().isnumeric() and mo_l.group().isalpha())
            print(f'So you are searching for files that weight over that {mo_n.group()} {mo_l.group()}')
            data = []
            data.append(int(mo_n.group()))
            data.append(mo_l.group())
            return data
    else:
        print('ehh wrong data ehh')
        input_value()


def to_bytes_converter():
    data = spliter(input_value())
    size_to_bytes = data[0]
    size_unit = data[1]
    # print(data)
    if size_unit.upper() == SIZE_UNIT.KB.value:
        size_to_bytes = size_to_bytes * 1024
    elif size_unit.upper() == SIZE_UNIT.MB.value:
        size_to_bytes = size_to_bytes * 1024 * 1024
    elif size_unit.upper() == SIZE_UNIT.GB.value:
        size_to_bytes = size_to_bytes * 1024 * 1024
    # print(size_in_bytes)
    data.append(size_to_bytes)
    data[1] = size_unit.upper()
    return data

def rev_converter(size_in_bytes, size_unit):
    if size_unit.upper() == SIZE_UNIT.KB.value:
        size_in_bytes = size_in_bytes / 1024
    elif size_unit.upper() == SIZE_UNIT.MB.value:
        size_in_bytes = size_in_bytes / (1024 * 1024)
    elif size_unit.upper() == SIZE_UNIT.GB.value:
        size_in_bytes = size_in_bytes / (1024 * 1024 * 1024)
    return size_in_bytes

def going_through_dir():
    data = to_bytes_converter()
    size = data[0]
    size_unit = data[1]
    size_in_bytes = data[2]
    filelist = []
    for folder, subfolders, files in os.walk('.'):
        for filename in files:
            filepath = os.path.join(os.path.abspath('.'), filename)
            size_of_file = os.path.getsize(filepath)
            size_of_file_in_proper_unit = rev_converter(size_of_file, size_unit)
            if size_of_file >= size_in_bytes:
                print(f'* {filename}  -->  {round(size_of_file_in_proper_unit, 2)} {size_unit}')
                filelist.append(filepath)
    return filelist

def deal_with_big_files():
    filelist = going_through_dir()

    
    while True:
        option = input('Do you want to delete this files, bro? (y\\n)\n')
        if option.upper() == 'Y':
            for file in filelist:
                print(f'{file} has been deleted')
                send2trash.send2trash(file)
            print('ok, work is done. all big files are in the trash right now')
            sys.exit()
        elif option.upper() == 'N':
            print('ok, bye, bro')
            sys.exit()
        else:
            print('incorrect option, please read carefully, you dummy')
            continue
        




deal_with_big_files()
        
