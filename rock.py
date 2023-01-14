import random

# Initializing the scores
player_score = 0
computer_score = 0

# list of possible choices
choices = ["rock", "paper", "scissors"]

while True:
    # get player's choice
    player = input("Choose rock, paper, or scissors (or quit to stop playing): ")
    if player.lower() == "quit":
        break
    if player.lower() not in choices:
        print("Invalid choice, please try again")
        continue

    # get computer's choice
    computer = random.choice(choices)

    # compare choices and determine winner
    if player == computer:
        print("It's a tie!")
    elif (player == "rock" and computer == "scissors") or (player == "paper" and computer == "rock") or (player == "scissors" and computer == "paper"):
        print("You win!")
        player_score += 1
    else:
        print("Computer wins!")
        computer_score += 1

    print("Player: {}  Computer: {}".format(player_score, computer_score))

# Print the final scores
print("Player: {}  Computer: {}".format(player_score, computer_score))
