'''
# Hello everyone, so this is my way of code to make a Rock, Paper, Scissors! game using python as a begineer
#if it is rocks then it will win scissors.
#if it is papers then it will win rock.
#if it is scissors them it will paper.
#if its rock and rock or paper and paper or scissor and scissor then its a draw!
'''

import random


def get_user_choice():
    while True:
        user_choice = input(
            "Enter your choice (rock, paper, or scissors): ").lower()
        if user_choice in ("rock", "paper", "scissors"):
            return user_choice
        else:
            print("Invalid choice. Please enter either 'rock', 'paper', or 'scissors'.")


def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])


def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a DRAW!"
    elif (
        (user_choice == "rock" and computer_choice == "scissors") or
        (user_choice == "paper" and computer_choice == "rock") or
        (user_choice == "scissors" and computer_choice == "paper")
    ):
        return "HURRAY!, You WIN! the game."
    else:
        return "OOPS!, Computer WINS! the game."


def main():
    print("Welcome to Rock, Paper, Scissors!")
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()
    print(f"You chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")
    result = determine_winner(user_choice, computer_choice)
    print(result)


if __name__ == "__main__":
    main()

while True:
    want_to_continue = input("Do you want to exit?\nYes or No...")
    if want_to_continue == "yes":
        break
    elif want_to_continue == "no":
        main()
    else:
        print("Enter either yes or no.")
