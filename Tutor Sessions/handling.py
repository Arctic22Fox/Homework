import os

# open the file in read mode with 'r'
infile=open('myfile.txt','r')
# reads the entire file
print(infile.read())
# close the file
infile.close()

print(' ')

# readline
infile2=open('myfile.txt','r')
line=infile2.readlines()
print(line)
infile2.close()

print(' ')

# read the whole file
lines = open('myfile.txt').read()
print(lines)

print(' ')

lines = open('myfile.txt').read().splitlines()
print(lines)

print(' ')

# safer recommended way to open files
with open('myfile.txt','r') as infile:
    for line in infile:
        print(line, end='')

print(' ')

infile = open('myfile.txt','r').read()
print(infile)

# writing to a file
output = open('myfile.txt','w')
output.write('7\n')
output.close()

# append to a file
output2 = open('myfile.txt','a')
output2.write('8\n')

# write list items without line terminators
fruit = ['oranges', 'mangoes']
output2.writelines(fruit)

# write list items to different lines
fruit = ['oranges\n', 'mangoes\n']
output2.writelines(fruit)

for fruit in fruit:
    output2.write(fruit)
    output2.write('\n')

# varFruit = 'banana'

output2.write('pineapple,banana')

# output2.close()

# os.remove('myfile.txt')

append = open('countries.txt','a')
append.write('UK\n', 'US\n', 'Africa\n', 'Russia\n', 'Australia\n')
append.close()

