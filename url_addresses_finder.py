#! python
# this script help you find the url addresses in http:// and https:// formats from your clipboard
# X 2020 Arnold Cytrowski

import pyperclip, re

text = str(pyperclip.paste())
matches = []

url_reg = re.compile(r'https?://\S+')

for groups in url_reg.findall(text):
    matches.append(groups)

if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('addreses has been copied into clipboard')
    print('\n'.join(matches))
else:
    print('there are not any url addresses here, sorry')