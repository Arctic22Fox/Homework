# importing the getpass from sys
import getpass

# maximum number of attempts for the input
max_attempts = 3
# correct PIN
pin = '1990'
# starting the attempts at 0
attempts = 0
# this allows the user to decide whether they want to protect/hide the PIN when they input it into the console. if they choose y the code will protect the PIN, else if they say anything other than y the code will show the PIN as they type
protect = input('Do you want to hide your PIN? (y/n: ')
# if the user inputs
if protect == 'y':
    while attempts < max_attempts:
        # the below prompts are asking the user to input their PIN (the hardcoded PIN), input does not block out the number that user is inputting. Where getpass makes the input private.
        # supplied_pin = input("Enter your PIN: ")
        supplied_pin = getpass.getpass("Enter your PIN: ")
        # if the correct PIN is supplied
        if supplied_pin == pin:
            print('PIN Accepted.')
            # exit the loop if the PIN is entered correctly
            break
        # otherwise this will run for a max of 3 attempts
        else:
            # increase the number of attempts by the user
            attempts += 1
            remaining_attempts = max_attempts - attempts
            if remaining_attempts > 0:
                print('Invalid PIN:', remaining_attempts, 'attempts remaining')
            else:
                print('Access Denied')

        if attempts == max_attempts:
            print('Max attempts reached. Your card has now been swallowed up. Goodbye.')
# if the user decides not to hide their PIN this script will allow the user to see the PIN they are entering
else:
    while attempts < max_attempts:
        # the below prompts are asking the user to input their PIN (the hardcoded PIN), input does not block out the number that user is inputting. Where getpass makes the input private.
        supplied_pin = input("Enter your PIN: ")
        # supplied_pin = getpass.getpass("Enter your PIN: ")

        if supplied_pin == pin:
            print('PIN Accepted.')
            # exit the loop if the PIN is entered correctly
            break

        else:
            # increase the number of attempts by the user
            attempts += 1
            remaining_attempts = max_attempts - attempts
            if remaining_attempts > 0:
                print('Invalid PIN:', remaining_attempts, 'attempts remaining')
            else:
                print('Access Denied')
    # if the PIN is not inputted correctly then this messages will appear after 3 attempts
    if attempts == max_attempts:
        print('Max attempts reached. Your card has now been swallowed up. Goodbye.')
        