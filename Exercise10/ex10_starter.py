import sys, glob, os

# Get the directory name
if sys.platform == 'win32':
    hdir = os.environ['HOMEPATH']
else:
    hdir = os.environ['HOME']

# Construct a portable wildcard pattern
pattern = os.path.join(hdir,'*')

file_list = glob.glob(pattern)

# using os.path.basename()

# TODO: Use the glob.glob() function to obtain the list of filenames
print(glob.glob(pattern))
list = (glob.glob(pattern))
for x in list:
    print(x, os.path.getsize(x))

print(' ')

# TODO: use os.path.getsize to find each file's size
while os.path.getsize(x) > 0:
    print(x, os.path.getsize(x))
    break

print(' ')

# TODO: Add a test to only display files that are not zero length

for x in list:
    if os.path.getsize(x) > 0:
        print(x, os.path.getsize(x))

print(' ')

# TODO: Remove the leading directory name(s) from each filename before you print it -

for x in list:
    print(os.path.basename(x), os.path.getsize(x))

print(' ')

for x in list:
    if os.path.getsize(x) > 0:
        print(os.path.basename(x), os.path.getsize(x))

print(' ')

import getpass

# maximum number of attempts for the input
max_attempts = 3
pin = '1990'

attempts = 0

while attempts < max_attempts:
    # supplied_pin = input("Enter your PIN: ")
    supplied_pin = getpass.getpass("Enter your PIN: ")

    if supplied_pin == pin:
        print('PIN Accepted.')
        break
    else:
        attempts += 1
        remaining_attempts = max_attempts - attempts
        if remaining_attempts > 0:
            print('Invalid PIN:', remaining_attempts, 'attempts remaining')
        else:
            print('Access Denied')

if attempts == max_attempts:
    print('Max attempts reached. Goodbye.')


