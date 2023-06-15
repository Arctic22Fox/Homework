import getpass

# maximum number of attempts for the input
max_attempts = 3
pin = '1990'

attempts = 0

while attempts < max_attempts:
    # supplied_pin = input("Enter your PIN: ")
    supplied_pin = getpass.getpass("Enter your PIN: ")

    if supplied_pin == pin:
        print('PIN Accepted.')
        break
    else:
        attempts += 1
        remaining_attempts = max_attempts - attempts
        if remaining_attempts > 0:
            print('Invalid PIN:', remaining_attempts, 'attempts remaining')
        else:
            print('Access Denied')

if attempts == max_attempts:
    print('Max attempts reached. Goodbye.')