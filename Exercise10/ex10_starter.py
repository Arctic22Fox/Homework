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