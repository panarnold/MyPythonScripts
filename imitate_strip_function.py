#! python
# this script imitate .strip() function, and it accepts one of two arguments:
# if user give it one argument -script will delete whitespaces from the beggining and the end of the text
# if user give it also second argument - it delete signs from second argument in given string

import re
from typing import Optional


def imitate_strip(given_text: str, optional_regex: Optional[str] = None):
    result_text = given_text
    if optional_regex:
        result_text = re.sub(optional_regex, '', result_text)
    else:
        result_text = re.sub(r'^\s+', '', result_text)
        result_text = re.sub(r'\s+$', '', result_text)
    print(result_text)

# def geet(first_name: str, last_name: Optional[str] = None):
#     print(f"witam ciebie {first_name} {last_name if last_name else ''}")

imitate_strip('    chuj mi  w ryuj example')
