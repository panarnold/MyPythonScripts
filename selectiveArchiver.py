#! python
# this script will archive everything except format you give in the argument
# X 2020 Arnold Cytrowski

import os, zipfile

def archiveIt():
    abs_directory_path = os.path.abspath('.')
    format = input('Give here format which you want to archive from this folder:\n')
    zip_new_file = zipfile.ZipFile(f'zipOf{format}.zip', 'w')
    if len(format) <= 3:
        for folder, subfolders, filenames in os.walk('.'):
            for filename in filenames:
                if filename.endswith(f'.{format}'):
                    print(f'{filename} has beed added to archive')
                    zip_new_file.write(os.path.join(abs_directory_path, filename), filename)
    print('muchas gracias amigo, have a great day')

archiveIt()

