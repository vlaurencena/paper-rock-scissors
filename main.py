import random

while True:

    choices = ["rock", "paper", "scissors"]

    computer_choice = random.choice(choices)
    player_choice = None

    while player_choice not in choices:
        player_choice = input("Rock, paper, or scissors?: ").lower()

    print("Computer picked "+ computer_choice +".")

    if player_choice == computer_choice:
        print("Tie!")

    elif player_choice == "rock":
        if computer_choice == "paper":
            print("You lose!")
        elif computer_choice == "scissors":
            print("You win!")

    elif player_choice == "paper":
        if computer_choice == "rock":
                print("You win!")
        elif computer_choice == "scissors":
                print("You lose!")

    elif player_choice == "scissors":
        if computer_choice == "rock":
                print("You lose!")
        elif computer_choice == "paper":
                print("You win!")

    play_again = input("Play again? (y/n):").lower()
    if play_again != "y":
        break

print("Thanks for playing! Bye!")