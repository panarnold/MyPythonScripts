#! python
# this script will test your password. It can give you the mark from the 0 to 3:
# 0 - password is weak as hell
# 3 - password strong like Mariusz 'Dominator' Pudzianowski
# three categories: 1st - at least 8 characters, 2nd - lower and upper case characters, 3rd - at least one digit
# X 2020 Arnold Cytrowski

import re
from re import search

white_space_reg = re.compile(r'\s+')
eight_char_reg = re.compile(r'\w{8,}')
low_upp_reg = re.compile(r'[A-Z]+[a-z]+')
dig_reg = re.compile(r'\d+')




while True:
    password = input('put here your password, boi\n')
    mark_count = 0
    if re.search(white_space_reg, password):
        print(f'your password {password} cannot have any whitespaces, boi')
        continue
    if re.search(eight_char_reg, password):
        mark_count += 1
    if re.search(low_upp_reg, password):
        mark_count += 1
    if re.search(dig_reg, password):
        mark_count += 1
    print(f'Your password {password} is {str(mark_count)} out of 3')
    break





