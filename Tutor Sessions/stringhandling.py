# Basic String
someString = 'Some String'

print(' ')

# Multiple line string
SomeString1 = """
First line
Multiple Strings
Third Line
"""

print(someString)
print(SomeString1)

print(' ')

# String character sequence position, printing a specific letter, positions start at 0
print(someString[0])
print(someString[2])

print(' ')

# String length, this is an integer, it will tell you the length of the string
print(len(someString))

print(' ')

# loop over a string
for x in someString:
    print(x)

print(' ')

# Some string methods
number = 3
astring = '3'
# you can change a string to integer or visa versa by prefixing with int or str
print(number + int(astring))

print(' ')

# print the string to uppercase or lowercase
print(someString.upper())
print(someString.lower())

print(' ')

# type your full names seperated by commas into a string variable and print the uppercase and lowercase instances of the string, print length of the combined names.
fullname = 'lewis, cleveland'

print(fullname.upper())
print(fullname.lower())
print(len(fullname))

print(' ')

# replacing
fullname = 'lewis, cleveland'
print(fullname.replace('lewis','alan'))
print(fullname)

print(' ')

# searching a string
print(fullname.find('cleveland'))

print('x' in fullname)

print(' ')

# slicing - substring, this is picking part of the string, a start and an end seperated by a colon
print(fullname[0:5])

print(' ')

# slice from start to a position, indicated by no input, or going to the end when you specify a start
print(fullname[:5])
print(fullname[7:])

print(' ')

# strip or remove whitespaces - strip, rstrip and lstrip
names = '      John, Doe    '
print(names)
print(names.strip())
# removed whitespace to the right
print(names.rstrip())
# remove whitespace to the left
print(names.lstrip())

print(' ')

# concatenate strings
firstname = 'Lewis'
lastname = 'Cleveland'
full = firstname + ' ' + lastname
print(full)
# adding a seperate variable in the concatenation
full = firstname + ' ' + lastname + ' MCIJ'
print(full)
age = 32
message = 'I am ' + str(age) + ' years old'
print(message)

print(' ')

# string formatting with placeholders and arguments
message1 = 'I am {} years old'
print(message1.format(age))

message2 = 'I am {} years old, and I like {}'
print(message2.format(age, 'Lego'))

print(' ')

# endswith and startswith
message3 = 'Welcome to Python'
print(message3.startswith('Welcome'))
print(message3.endswith('Python'))

print(message3.startswith('e'))
print(message3.endswith('o'))

print(' ')

# split a string into a list
message4 = 'Welcome to Pytons coolness'
print(message4.split())

print(' ')

message4 = 'Welcome to Pytons coolness'
splitlist = message4.split()
for x in splitlist:
    print(x)

# split using characters
message4 = 'Welcome, to, Pytons, coolness'
splitlist = message4.split(',')
for x in splitlist:
    print(x)

# escape characters
message5 = 'Hello World, it is \'sunny\' today'
print(message5)
# new line character
message6  = 'Hello World, it is \nsunny \ntoday'
print(message6)
