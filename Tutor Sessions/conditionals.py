a = 2
b = 3

# if

# logical operators not equal !=
if a==b:
    print('a is equal to b')
else:
    print('a is not equal to b')

# if statement on a list item
lang= ['Perl', 'Python', 'PHP', 'Ruby']
if 'Python' in lang:
    print('Python is found')

# else if (elif)
# is a equal to b, no this will not print
if a==b:
    print('a is equal to b')
# is a greater than b, no so this will not print
elif a>b:
    print('a is greater than b')
# therefor the above statements are not true so this statement will print
else:
    print('Some other unexpected condition')

# chained conditions
number=5
distance=42
# number is greater than 0 but distance is equal to 42, this will not print
if 0 < number <42 < distance:
    print('num and dist are within range')
# this will print as the statement is false
else:
    print('num and dist are out of range')

# logical AND operator on chained conditionals
if 0 < number and number < 42 and 42 < distance:
    print('num and dist are within range')

myList = [1,2,3,5,7,9]
if myList:
    print('The list is not empty')
# use of the NOT operator, this will give the opposite. as these are all NOT 0
myList2 = [0,1,2,3]
if not all(myList2):
    print('not all are true')

myList2 = [0,1,2,3]
if any(myList2):
    print('at least one item is true')

print(' ')

# Object types
num = 42
txt = '3'
# here I have changed the string to an integer to allow the program to run with no error
if int(txt) < num:
    print('txt is less than num')

print(' ')

# while
line = None
while line != 'done':
    line = input('type "done" to complete:')
    print('<', line, '>')

i = 1
while i < 8:
    print(i)
    if i == 4:
        print('The value of i is 4')
    i+=1

# while with break
i = 1
while i < 8:
    print(i)
    if i == 4:
        break
    i+=1

print('')
print('')

# while with continue - continue to the next iteration
i = 1
while i < 8:
    i+=1
    if i == 4:
        continue
    print(i)

# while with else
i = 1
while i < 8:
    i+=1
    print(i)
else:
    print('i is no longer less than 8')

# for loops
# Each element of the fruits list is assigned to the variable x in each iteration of the loop, and then it is printed using the print() function.
fruits = ['apple', 'banana', 'orange', 'grape']
for x in fruits:
    print(x)
    if x =='orange':
        break
# The loop iterates over each element in the fruits list. When the variable x is assigned the value 'orange', the condition x == 'orange' evaluates to True. As a result, the code executes the print(x) statement and then encounters the break statement. The break statement exits the loop immediately, so the remaining fruits ('grape' in this case) are not processed or printed.

print(' ')

foods = ['pizza', 'pasta', 'soup', 'sweets', 'crisps']
for x in foods:
    print(x)
    if x.startswith('so'):
        break

print(' ')

for x in 'banana':
    print(x)

print(' ')

# In each iteration of the loop, the variable i takes on the values from 0 to the length of some_list minus 1. The len(some_list) function returns the number of elements in the list.
# The condition if i == 2: checks if the value of i is equal to 2. If it is, the break statement is executed, which terminates the loop immediately. This means that the loop will only iterate for the first two elements of the list.
# The print(some_list[i], i) statement within the loop prints the current element of some_list and its corresponding index i.
some_list=['John', 'Jack', 'Jim', 'Joe']
for i in range(0,len(some_list)):
    if i ==2:
        break
    print(some_list[i], i)

print(' ')

# range with step
# In each iteration of the loop, the variable x takes on the values from 2 up to (but not including) 20, incrementing by 2 in each step. The code block inside the loop will be executed for each value of x.
for x in range(2, 20, 2):
    print(x)
else:
    print('Finished')

# In each iteration of the loop, the variable x takes on the values starting from start (which is 2) up to, but not including, end (which is 20), incrementing by step (which is 3) in each step.
# The print(x) statement within the loop prints the current value of x for each iteration.
# After the loop completes, the code block within the else statement is executed, regardless of whether the loop completed normally or was interrupted by a break statement.

start = 2
end = 20
step = 3

for x in range(start, end, step):
    print(x)
else:
    print('Finished')