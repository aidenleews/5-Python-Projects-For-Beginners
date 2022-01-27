import random

user_wins = 0
computer_wins = 0

options = ["rock", "paper", "scissors"]

while True:
    user_input = input("Type Rock/Paper/Scissors or Q to quit: ").lower()

    # Finishing the game
    if user_input == "q":
        break

    # Typo check (User input restriction)
    if user_input not in options:
        print("Invalid input.")
        continue

    # Game continues
    random_number = random.randint(0, 2)  # Rock: 0, Paper: 1, Scissors: 2
    computer_pick = options[random_number]
    print("Computer:", computer_pick)

    # User VS Computer
    if user_input == computer_pick:
        print("Play again!")
        continue
    elif user_input == "rock" and computer_pick == "scissors":
        print("You won!")
        user_wins += 1
    elif user_input == "paper" and computer_pick == "rock":
        print("You won!")
        user_wins += 1
    elif user_input == "scissors" and computer_pick == "paper":
        print("You won!")
        user_wins += 1
    else:
        print("You lost!")
        computer_wins += 1
    continue

print("You won", user_wins, "times / Computer won", computer_wins, "times.")
