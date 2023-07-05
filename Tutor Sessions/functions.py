# def is short for define, to define the function name
def first_function():
    print('my very first python function')
    print('here is my second text in my function')
# call the function to be actioned in the terminal
first_function()

# parsing arguments to functions
def second_function(firstname):
    print('my name is '+ firstname)

second_function('Lewis')
second_function('Alan')

# ERROR occurs because argument not supplied
# second_function()

def third_function(firstname, lastname):
    print('my first name is ' + firstname + ' ' + lastname)

# ERROR occurs because not all arguments have been supplied
# third_function('Cleveland')

# unspecified number of parameters
def fourth_function(*params):
    print('the number of arguments is ' + str(len(params)) + ' and the first item in our argument list is ' + params[0])

fourth_function('test')
fourth_function('test2','test')

def fifth_function(first_name, last_name):
    print('My full name is ' + first_name + ' ' + last_name)

fifth_function(first_name='Lewis',last_name='Cleveland')

# multiple arguments with unspecified parameter names
def sixth_function(**params):
    print('the first argument is ' + params['name'] + ' and second is ' + params['lname'])

sixth_function(name='Lewis', lname='Cleveland')

# default parameters
def seventh_function(age=25):
    print('my name is ' + str(age))

seventh_function(30)
seventh_function()

listofcountries = ['UK','Germany', 'Spain']

def countries_function(countries):
    print('the number of countries is ' + str(len(countries)) + ' countries and they are;')
    for x in countries:
        print(x)

countries_function(listofcountries)

# functions using return keyword

def number(num):
    return num

print(number(5))
somenumber = number(5)

print(somenumber)

# functions with empty body. use pass keyword to avoid compiler errors
def somefunction():
    pass

# recursion  - a function calling itself
def factorial(num):
    if num == 1:
        return 1
    else:
        return (num*factorial(num-1))

number = 6
print('the factorial of ' + str(number) + ' is ' + str(factorial(6)))

# variable visibilty in functions

result = 3

def scope_test1():
    result = 42

scope_test1()
print(result)


def scope_test2():
    global result
    result = 42


scope_test2()
print(result)

