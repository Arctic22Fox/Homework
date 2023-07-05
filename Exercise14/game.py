import random

# Function to get the user's choice
def get_user_choice():
    choice = input("Enter your choice (rock, paper, scissors, lizard, or Spock): ")
    # Validate the user's input
    while choice.lower() not in ['rock', 'paper', 'scissors', 'lizard', 'spock']:
        choice = input("Invalid input. Please enter rock, paper, scissors, lizard, or Spock: ")
    return choice.lower()

# Function to get the computer's choice
def get_computer_choice():
    choices = ['rock', 'paper', 'scissors', 'lizard', 'spock']
    # Randomly select a choice for the computer
    return random.choice(choices)

# Function to determine the winner
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    # Check the winning conditions for the user
    elif (user_choice == 'rock' and (computer_choice == 'scissors' or computer_choice == 'lizard')) or \
         (user_choice == 'paper' and (computer_choice == 'rock' or computer_choice == 'Spock')) or \
         (user_choice == 'scissors' and (computer_choice == 'paper' or computer_choice == 'lizard')) or \
         (user_choice == 'lizard' and (computer_choice == 'paper' or computer_choice == 'Spock')) or \
         (user_choice == 'spock' and (computer_choice == 'rock' or computer_choice == 'scissors')):
        return "You win!"
    # If the above conditions are not met, computer wins
    else:
        return "Computer wins!"

# Function to check if the user wants to play again
def play_again():
    choice = input("Do you want to play again? (yes/no): ")
    return choice.lower() == 'yes'

# Function to play the game
def play_game():
    print("Let's play Rock-Paper-Scissors-Lizard-Spock!")
    while True:
        user_choice = get_user_choice() # Get user's choice
        computer_choice = get_computer_choice() # Get computer's choice
        print(f"\nYou chose: {user_choice}")
        print(f"Computer chose: {computer_choice}")
        print(determine_winner(user_choice, computer_choice)) # Determine the winner
        if not play_again():
            break

# Start the game
play_game()
