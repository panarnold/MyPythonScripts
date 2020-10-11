#! python
#mcb pyw - script can save and load text to/from your clipboard
# example1: py.exe mcb.pyw save <keyword> --- save content of current clipboard with its key <keyword>
# example2: py.exe mcb.pyw <keyword> --- load content of <keyword> to the clipboard
# example3: py.exe mcb.pyw list --- print the list of cureent keywords
# example4: py.exe mcb.pyw delete <keyword> --- delete content of <keyword>
# example5: py.exe mcb.pyw delete --- delete all keywords
# X 2020 Arnold Cytrowski

import shelve, pyperclip, sys

mcbShelf = shelve.open('mcb')

if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
    mcbShelf[sys.argv[2]] = pyperclip.paste()
elif len(sys.argv) == 3 and sys.argv[1].lower == 'delete':
    if sys.argv[2] in mcbShelf:
        del mcbShelf[sys.argv[2]]
elif len(sys.argv) == 2:
    if sys.argv[1].lower() == 'list':
        pyperclip.copy(str(list(mcbShelf.keys())))
    elif sys.argv[1].lower() == 'delete':
        mcbShelf.clear()
    elif sys.argv[1] in mcbShelf:
        pyperclip.copy(mcbShelf[sys.argv[1]])




mcbShelf.close()