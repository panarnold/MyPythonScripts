#! python
# addprefix - program responsible for adding prefixes before name of every file in the current direction
# X 2020 Arnold Cytrowski

import shutil, os, re

def addPrefix():
    prefix = re.compile(input('Put ur prefix here:\n'))

    for original_name in os.listdir('.'):

        if os.path.isfile(original_name):

            abs_working_dir = os.path.abspath('.')
            original_file_name = os.path.join(abs_working_dir, original_name)
            new_prefix_name = os.path.join(abs_working_dir, prefix)

            print(f'renaming {original_file_name} to {new_prefix_name}')

            shutil.move(original_file_name, new_prefix_name)

addPrefix()

    