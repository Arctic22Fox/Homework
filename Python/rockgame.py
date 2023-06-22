import random

def play_game():
    choices = ['rock', 'paper', 'scissors', 'lizard', 'spock']

    user_choice = input("Enter your choice: ").lower()
    while user_choice not in choices:
        print("Invalid choice. Please try again.")
        user_choice = input("Enter your choice: ").lower()

    computer_choice = random.choice(choices)
    print(f"Computer's choice: {computer_choice}")

    if user_choice == computer_choice:
        print("It's a tie!")
    elif user_choice == 'rock':
        if computer_choice == 'scissors' or computer_choice == 'lizard':
            print("You win!")
        else:
            print("Computer wins!")
    elif user_choice == 'paper':
        if computer_choice == 'rock' or computer_choice == 'spock':
            print("You win!")
        else:
            print("Computer wins!")
    elif user_choice == 'scissors':
        if computer_choice == 'paper' or computer_choice == 'lizard':
            print("You win!")
        else:
            print("Computer wins!")
    elif user_choice == 'lizard':
        if computer_choice == 'paper' or computer_choice == 'spock':
            print("You win!")
        else:
            print("Computer wins!")
    elif user_choice == 'spock':
        if computer_choice == 'rock' or computer_choice == 'scissors':
            print("You win!")
        else:
            print("Computer wins!")
    else:
        print("Invalid choice.")


# Let's Play
play_game()
