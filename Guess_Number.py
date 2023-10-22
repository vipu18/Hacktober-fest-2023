import random

def guessing_game():
    secret_number = random.randint(1, 20)
    attempts = 0
    max_attempts = 5

    print("Welcome to the Guessing Game!")
    print("I'm thinking of a number between 1 and 20.")

    while attempts < max_attempts:
        guess = int(input("Take a guess: "))
        attempts += 1

        if guess < secret_number:
            print("Too low!")
        elif guess > secret_number:
            print("Too high!")
        else:
            print(f"Good job! You guessed the number in {attempts} attempts!")
            break

    if guess != secret_number:
        print(f"Sorry, the number I was thinking of was {secret_number}. Better luck next time!")

# Run the game
guessing_game()