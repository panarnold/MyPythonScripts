#! python
# backup_to_zip.py - put the cwd with its content into ZIP. Names of the next ZIPS are incremented
# every fuckin' time
# X 2020 Arnold Cytrowski

import zipfile, os

def backup_to_zip(folder):

    folder = os.path.abspath(folder)

    number = 1
    while True:
        zip_file_name = f'{os.path.basename(folder)}_{str(number)}.zip'
        if not os.path.exists(zip_file_name):
            break
        number += 1

    print(f'Creating archive "{zip_file_name}"')
    backup_zip = zipfile.ZipFile(zip_file_name, 'w')

    print('aaaand it is done')