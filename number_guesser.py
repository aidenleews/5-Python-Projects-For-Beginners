import random

# User input restriction to positive integers
while True:
    top_of_range = input('Give me a number: ')
    try:
        top_of_range = int(top_of_range)
        if top_of_range > 0:
            print("You have to guess a number between 0 -", top_of_range)
            break  # Getting out of the loop for the main game
        else:
            print('Give me a number bigger than 0.')
            continue
    except ValueError:
        print('Number only please.')  # User input is not an integer
        continue

# Main game
random_number = random.randint(0, top_of_range)
guesses = 0

while True:
    user_guess = input('Your guess: ')
    try:
        user_guess = int(user_guess)
        guesses += 1
        if user_guess == random_number:
            print('You got it!')
            break
        elif user_guess < random_number:
            print('Above')
            continue
        else:
            print('Below')
            continue
    except ValueError:
        print('Number only please.')  # Not an integer
        continue

print("You got it in", guesses, "guess(es).")
