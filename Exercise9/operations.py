var = input("Please enter a value: ")

# .upper is a method that makes the input text uppercase
print(var.upper())

# adding len (length function) looks at the length of the users input
character = len(var)
print("number of characters: ", character)

# if the value is a whole number this returns true, if anything else, this is false
print(var.isdecimal())