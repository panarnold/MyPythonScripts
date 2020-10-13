#! rename_dates.py - script responsible for changing name of the file which contains american-format-date
# (MM-DD-RRRR) to european-format-date (DD-MM-RRRR)

import shutil, os, re


def fromUSAtoEUR():
    date_pattern = re.compile(r'''
    ^(.*?)
    ((0|1)?\d)-
    ((0|1|2|3)?\d)-
    ((19|20)\d\d)
    (.*?)$
    ''', re.VERBOSE)

    for amer_file_name in os.listdir('.'):
        mo = date_pattern.search(amer_file_name)

        if mo == None:
            continue

        before_part = mo.group(1)
        month_part = mo.group(2)
        day_part = mo.group(4)
        year_part = mo.group(6)
        after_part = mo.group(8)

        euro_file_name = f'{before_part}{day_part}-{month_part}-{year_part}{after_part}'

        abs_working_dir = os.path.abspath('.')
        amer_file_name = os.path.join(abs_working_dir, amer_file_name)
        euro_file_name = os.path.join(abs_working_dir, euro_file_name)

        print(f'renaming "{amer_file_name}" to "{euro_file_name}"')
        shutil.move(amer_file_name, euro_file_name)

def fromEURtoUSA():
    date_pattern = re.compile(r'''
    ^(.*)? #something before
    ((1|2|3)?\d)- #day of month, group 2 and 3
    ((0|1)?\d)- # month, group 4 and 5
    ((19|20)\d\d) #year, group 6 and 7
    (.*)?$ # group 8
    ''', re.VERBOSE)

    for eur_filename in os.listdir('.'):
        mo = date_pattern.search(eur_filename)

        if mo == None:
            continue

        before_part = mo.group(1)
        day_part = mo.group(2)
        month_part = mo.group(4)
        year_part = mo.group(6)
        after_part = mo.group(8)

        usa_filename = f'{before_part}{month_part}-{day_part}-{year_part}{after_part}'

        abs_dir_name = os.path.abspath('.')
        eur_full_filename = os.path.join(abs_dir_name, eur_filename)
        usa_full_filename = os.path.join(abs_dir_name, usa_filename)
        
        print(f'renaming from {eur_full_filename} to {usa_full_filename}')
        shutil.move(eur_full_filename, usa_full_filename)


