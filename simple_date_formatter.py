#! python
# this little script is responsible for finding the dates in the text and transform them
# into one specific format
# X 2020 Arnold Cytrowski

import pyperclip, re, copy



text = str(pyperclip.paste())

re_S = re.compile(r'(\S+)')

items = re_S.split(text)

matched_dates = []

date_reg = re.compile(r'(\d{1,4})(-|\.|\\)(\d{1,2})(-|\.|\\)(\d{1,4})')



for groups in date_reg.findall(text):
    nice_date = '-'.join([groups[0], groups[2], groups[4]])
    if (len(groups[4]) < len(groups[0])):
        nice_date = '-'.join([groups[4], groups[2], groups[0]])
    matched_dates.append(nice_date)

copied_dates = copy.copy(matched_dates)

for i in range(len(items)):
    if(date_reg.match(items[i])):
        items[i] = matched_dates[0]
        del matched_dates[0]

text = ''.join(items)

if len(copied_dates) > 0:
    pyperclip.copy(text)
    print('all dates has been modified and updated to dd-mm-yyyy format')
    print(text)
else:
    print('there was nothing to do, sorry')

    








