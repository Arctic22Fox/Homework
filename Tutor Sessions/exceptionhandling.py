# basic try-except block

# try - test some blocks of code
# except - handler errors when found in the blocks
# else - execute code when there is no error
# finally - execute code whether an error occurs or not

def divide(a,b):

        if b==0:
            raise ValueError("Error occurred : Division by Zero")

        try:

            result = a/b
            return result
    # # except ZeroDivisionError:
    # #     print("Error : Division by zero is not allowed")
    # # except TypeError:
    # #     print("Error : One of the values has a wrong type")
    # #     return None
    # except Exception as e:
    #     print("An unexpected error occurred with details" + str(e))
    #     return None
    # # else:
    #     print("no errors raised")
    # finally:
    #     print("finally block run")

firstNum = 5
secondNum = 2

    try:
        result = divide(firstNum, secondNum)
        print("resultis " + result)
    except ValueError as v:
        print(v)

result = divide(firstNum, secondNum)
print("result is :" + str(result))

