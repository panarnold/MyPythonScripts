#! python
# addBulletPointSirpy - it automatically take text sample from the clipboard, format that text by adding
#there a bulletpoint for every single row, and give it back to the clipboard.
# 10.2020 Arnold Cytrowski

import pyperclip
text = pyperclip.paste()

lines = text.split('\n')
for row in range(len(lines)):
    lines[row] = f'* {lines[row]}'
text = '\n'.join(lines)


pyperclip.copy(text)
