#! python
# this script is responsible for finding the fragile data (id, credit cards number) from
# the text in the clipboard and replacing them by '***' signs
# X 2020 Arnold Cytrowski

import re, pyperclip

text = str(pyperclip.paste())

pesel_reg = re.compile(r'\d{11}')

credit_card_reg = re.compile(r'(\d{4}[- ]){3}\d{4}|\d{16}')

text = pesel_reg.sub('*P*E*S*E*L*', text)
text = credit_card_reg.sub('*C*A*R*D*N*U*M*B*E*R*', text)


pyperclip.copy(text)

print('the changes has beed added succesfully')
print('here is your text afterwars (you have it updated in your clipboard): ')
print(text)

