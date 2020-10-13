#! python
# this script will archive all .txt files from the directory and it's full directory tree
# X 2020 Arnold Cytrowski

from os import walk
import zipfile, os

def backupTxtToZip(zipFolder):

    abs_directory_path = os.path.abspath('.')
    zip_folder_full_path = os.path.join(abs_directory_path, zipFolder)
    print(f'creating archives of *.txt files from current directory and it\'s curent tree into "{zipFolder}"' )
    txt_zip = zipfile.ZipFile(f'{zip_folder_full_path}.zip', 'w')

    for folder, subfolders, filenames in os.walk('.'):
        for filename in filenames:
            if filename.endswith('.txt'):
                print(filename)
                txt_zip.write(os.path.join(folder, filename))
    txt_zip.close()
    print('aaand it\'s done')


backupTxtToZip(input('give the name of the new zipfile:\n'))
    