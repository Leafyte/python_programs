#Design a Python program using Regular expressions to

# a) Extract Email IDs from a given text.

import re

text = """
xyz@gmail.com and 999@9ad.com and
abc.987@vvce.ac.in are the mail ids.
(897)-012-3456 ext.213 and 897.012-3456x23 are numbers
"""

emailRegex = re.compile(
    r'[a-zA-Z0-9._]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}'
)

L = emailRegex.findall(text)

for email in L:
    print(email)

# (Alternative Method)

import re

p = input("Input your password: ")

if len(p) > 5 and len(p) < 17 and re.search('[a-z]', p) \
and re.search('[A-Z]', p) and re.search('[0-9]', p) \
and re.search('[@#$-_]', p):

    print("Valid Password")

else:
    print("Invalid Password")

# b) Validate the user password with minimum length=6 and maximum length=16 and 
# must have at least one lower-case letter, upper-case letter, 
# number and special symbol (#, @, $, _).

import re

pwd = input("Enter a password: ")

if not len(pwd) > 5:
    print("Invalid Password")

elif not len(pwd) < 17:
    print("Invalid Password")

elif not re.search('[a-z]', pwd):
    print("Invalid Password")

elif not re.search('[A-Z]', pwd):
    print("Invalid Password")

elif not re.search('[0-9]', pwd):
    print("Invalid Password")

elif not re.search('[@#$-_]', pwd):
    print("Invalid Password")

else:
    print("Valid Password")

# (Alternative Method)

import re

emailRegex = re.compile(r'''
[a-zA-Z0-9._]+      # username
@                   # @ symbol
[a-zA-Z0-9.-]+      # domain name
[.]                 # dot
[a-zA-Z]{2,4}       # type
''', re.VERBOSE)

text = """
xyz@gmail.com and 123hello@yahoo.com and
more@vvce.ac.in and phone good +91 3478968421
are numbers
"""

L = emailRegex.findall(text)

for email in L:
    print(email)