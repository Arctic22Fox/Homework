# String handling in Python refers to the various operations and techniques used to manipulate and work with strings, which are sequences of characters.

# Python provides a rich set of built-in functions, methods, and operators that allow you to perform a wide range of string handling operations. Here are some common string handling operations in Python:

# 1. String Creation: You can create strings by enclosing characters within single quotes (''), double quotes ("") or triple quotes (""").
# Example:
my_string = 'Hello, World!'
print(my_string)

# 2. String Concatenation: You can concatenate (join) two or more strings together using the concatenation operator (+).
# Example:
string1 = 'Hello'
string2 = 'World'
result = string1 + ' ' + string2  # 'Hello World'
print(result)

# 3. String Length: You can find the length of a string using the built-in `len()` function.
# Example:
my_string = 'Hello'
length = len(my_string)  # 5
print(length)

# 4. String Indexing: You can access individual characters of a string using index positions. Indexing starts at 0 for the first character.
# Example:
my_string = 'Hello'
first_char = my_string[0]  # 'H'
print(first_char)

# 5. String Slicing: You can extract a portion of a string using slicing. It allows you to specify a range of indices to extract a substring.
# Example:
my_string = 'Hello, World!'
substring = my_string[7:12]  # 'World'
print(substring)

# 6. String Methods: Python provides several built-in string methods to perform operations like searching, replacing, splitting, converting case, etc. Some commonly used methods are `lower()`, `upper()`, `replace()`, `split()`, `find()`, `startswith()`, `endswith()`, and `join()`, among others.
# Example:
my_string = 'Hello, World!'
lower_case = my_string.lower()  # 'hello, world!'
replaced_string = my_string.replace('Hello', 'Hi')  # 'Hi, World!'
words = my_string.split(',')  # ['Hello', ' World!']
print(my_string)
print(lower_case)
print(replaced_string)
print(words)

# These are just a few examples of string handling in Python. Python's string handling capabilities are extensive, and there are many more functions and methods available to manipulate strings according to your needs.