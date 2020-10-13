#! python
# this script is responsible for renaming the files by deleting zeroes from its names
# e.g: spam0042.py --> spam42.py
# X 2020 Arnold Cytrowski

import re, shutil, os

for filename in os.listdir('.'):
    abs_directory_path = os.path.abspath('.')
    new_filename = re.sub('0', '', filename)
    full_filename = os.path.join(abs_directory_path, filename)
    new_full_filename = os.path.join(abs_directory_path, new_filename)

    print(f'Renaming {full_filename} to {new_full_filename}')
    shutil.move(full_filename, new_full_filename)