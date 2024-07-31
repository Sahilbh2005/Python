import random

def get_user_choice():
#Prompt user for choice and validate input.
    while True:
        user_input = input("Choose rock, paper, or scissors: ").lower()
        if user_input in ["rock", "paper", "scissors"]:
            return user_input
        else:
            print("Invalid choice. Please choose rock, paper, or scissors.")

def get_computer_choice():
#Generate random computer choice.
    return random.choice(["rock", "paper", "scissors"])

def determine_winner(user_choice, computer_choice):
#Compare choices and determine winner.
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        return "You win!"
    else:
        return "Computer wins!"

def main():
    user_score = 0
    computer_score = 0
 # Initialize the tie count
    tie = 0  
    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()

        print(f"\nYour choice: {user_choice}")
        print(f"Computer's choice: {computer_choice}")

        result = determine_winner(user_choice, computer_choice)
        print(result)

        if result == "You win!":
            user_score += 1
        elif result == "Computer wins!":
            computer_score += 1
        else:
            tie += 1

        print("\nScores:")
        print(f"Your score: {user_score}")
        print(f"Computer score: {computer_score}")
        print(f"Ties: {tie}")

        play_again = input("Play again? (yes/no): ").lower()
        if play_again != "yes":
            break

if __name__ == "__main__":
    main()
