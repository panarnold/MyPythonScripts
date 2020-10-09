#! python
# it's a simple program which is responsible for saving the boring passwords.
# program automatically paste the password from the value to clipboard - it makes easier
# for the user to paste it directly to the field which he want to put it
# it's not unsafe version, without the encryption, but in the future - who knows?
# @Arnold Cytrowski, X 2020

PASSWORDS = {
    'email' : 'iAMv33rySt00pid',
    'blog' : 'iW444ntt00D133',
    'safe' : '1v3g00t4l00tof$$yes1t5aj00k3'
}

import sys, pyperclip
if len(sys.argv) < 2:
    print('a password for this account has been copied into clipboard')
    sys.exit()

account = sys.argv[1]

if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print(f'Password to \'{account}\' account has been copied successfully')
else:
    print(f'There is no account which name is: {account}')

