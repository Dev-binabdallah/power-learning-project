# Individual Project: Rock, Paper, Scissors

- This a python program lets human player play against the computer. Ask the human for their choice, have the computer pick randomly, then announce the result (win, lose, or draw) with a clear message.
- If you've never played, here are the rules: two players each secretly choose Rock, Paper, or Scissors, then reveal their choice at the same time. The winner is decided like this:
1. Rock smashes Scissors → Rock wins
2. Scissors cut Paper → Scissors win
3. Paper covers Rock → Paper wins
4. If both players pick the same thing → it's a draw

- Rock, Paper, and Scissors are the only allowed choices.

# Code explanation:

1. import random — imports Python's random module so the computer can make a random choice.
2. options = ["rock", "paper", "scissors"] — creates a list of the three valid choices.
3. computer = random.choice(options) — randomly selects one option for the computer.
4. player = input(...).lower() — asks the player to enter a choice and converts it to lowercase.
5. if player not in options: — checks whether the player's choice is valid. If it isn't, the program asks for another choice.
6. if player == computer: — checks whether both chose the same option, resulting in a draw.

The three elif statements check all the situations where the player wins and else — if none of the winning conditions or the draw condition is true, the computer wins.