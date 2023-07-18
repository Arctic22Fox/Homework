# Write a program that takes two integers as input from the user and performs division. Implement exception handling to handle potential errors, such as division by zero or non-integer input.

def name_age(name, age):

        try:
                name = input("Enter your name: ")
                age = int(input("Enter your age: "))

                result = name, age
                return result
        except TypeError:
                print("Please input a valid type")
                return None
        except ValueError:
                print("Please input a valid number")
                return None



name_age("", 0)