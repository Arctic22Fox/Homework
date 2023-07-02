# this is a simple function that will print what is in the '', the string
print('I am Lewis Cleveland')

# this is a print funtion to print a simple dog
print('o----')
print(' ||||')

# the below will print a * 10 times
print('*' * 10)

# this is an example of a variable, price is the tag, 10 is an integer associated with the tag/variable
price = 10
# I can then change the price to 20, Python will read from top to bottom so will print the last price listed
price = 20
print(price)
# this is a float or decimal
rating = 4.9
# this is another string
name = 'Lewis'
# this is a boolean, they can either be True or False, the capital letters are important
is_published = True

# task: write variables for a patient called John Smith, hes 20 and is a new patient
fullname = 'John Smith'
age = 20
new_patient = True
# this is a input function for the user to answer
name = input('What is your name? ')
# this is an example of concatenation
print('Hi ' + name)

# task: ask 2 questions, persons name and favourite colour. then print the output
name = input('What is your name? ')
colour = input('Whats your favourite colour? ')
print(name + ' likes ' + colour)

# when we want to use the maths, you cannot take an int from a str, the string needs to be changed to an integer, or int
birth_year = input('What is your birth year? ')
age = 2023 - int(birth_year)
print(age)
# you can use the type function by typing (type)
print(type(age))

# challenge: gather a weight input, then to convert into pounds, so using the input, converting into int then times by 2.2
weight = input('What is your weight in kg? ')
pounds = int(weight) * 2.2
print(pounds)

