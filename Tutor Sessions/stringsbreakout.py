# write a python code that takes a string as an input and counts the number of vowels (a,e,i,o,u) in the string

string = 'I am Lewis and I Like Lego'
string = string.lower()
a = string.count('a')
e = string.count('e')
i = string.count('i')
o = string.count('o')
u = string.count('u')
vowels = a + e + i + o + u
print(vowels)

print(' ')

groupstring = 'I am Lewis and I Like Lego'
groupstring = groupstring.lower()
vowels = 'aeiou'
count = 0
for number in groupstring:
    if number in vowels:
        count += 1
print(count)

print(' ')

# write a python code that takes a string as input and returns the revers of the string (method to do it)
print(string[::-1])

print(' ')

# write a python code that takes a string as input and counts the words in the string. assume the words are seperated by spaces
list = string.split()
print(len(list))
