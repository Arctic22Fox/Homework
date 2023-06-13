#! /usr/bin/python

# Example Python script

import sys
# This is a command line/argument
# argv is part of the sys module
# argument vector aka the list of parameters or inputs to the program
# argc is our variable
argc = len(sys.argv)
#  'if' is called a condition expression
if argc > 1:
    print('Too many args')
else:
    # where is a variable whose value is a string 'World'
    where = 'World'
    print("hello", where)

print('Goodbye from ' +
      sys.argv[0])

# print(sys.argv[2])
# print(sys.argv[3])
# print(sys.argv[4])