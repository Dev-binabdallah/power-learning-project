import random

options = ["rock", "paper", "scissors"]
computer = random.choice(options)
player = input("Choose rock, paper, or scissors: ").lower()
while player not in options:
    print("Invalid option. Please choose from the option list.")
    player = input("Choose rock, paper, or scissors: ").lower()
if player == computer:
    print("It's a draw!")
elif player == "rock" and computer == "scissors":
    print("Rock smashes scissors. You win!")
elif player == "scissors" and computer == "paper":
    print("Scissors cut paper. You win!")
elif player == "paper" and computer == "rock":
    print("Paper covers rock. You win!")
else:
    print("Computer wins!")