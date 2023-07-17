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
def determine_winner(user, computer):
    if user == computer:
        return "It's a tie!"
    # Check the winning conditions for the user
    elif (user == 'rock' and (computer == 'scissors' or computer == 'lizard')) or \
         (user == 'paper' and (computer == 'rock' or computer == 'Spock')) or \
         (user == 'scissors' and (computer == 'paper' or computer == 'lizard')) or \
         (user == 'lizard' and (computer == 'paper' or computer == 'Spock')) or \
         (user == 'spock' and (computer == 'rock' or computer == 'scissors')):
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
    user_score = 0
    computer_score = 0
    while True:
        user_choice = get_user_choice() # Get user's choice
        computer_choice = get_computer_choice() # Get computer's choice
        print(f"\nYou chose: {user_choice}")
        print(f"Computer chose: {computer_choice}")
        result = determine_winner(user_choice, computer_choice) # Determine the winner
        print(result)
        if result == "You win!":
            user_score += 1
        elif result == "Computer wins!":
            computer_score += 1
        print(f"Score - You: {user_score}, Computer: {computer_score}")
        if not play_again():
            break

# Start the game
play_game()

