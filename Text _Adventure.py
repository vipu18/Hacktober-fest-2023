import time

# Function to simulate a delay for better text display1
def delay_print(text, delay=0.2):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def game_start():
    delay_print("Welcome to the Text Adventure Game!")
    delay_print("You find yourself in a dark and mysterious forest.")
    delay_print("You have two paths ahead of you. Which path will you choose?")
    delay_print("1. Take the left path")
    delay_print("2. Take the right path")

    choice = input("Enter your choice (1/2): ")

    if choice == '1':
        left_path()
    elif choice == '2':
        right_path()
    else:
        delay_print("Invalid choice. Please enter '1' or '2'.")
        game_start()

def left_path():
    delay_print("You chose the left path and walk deeper into the forest.")
    delay_print("You stumble upon a treasure chest!")
    delay_print("Do you want to open the chest?")
    delay_print("1. Open the chest")
    delay_print("2. Leave the chest alone")

    choice = input("Enter your choice (1/2): ")

    if choice == '1':
        delay_print("You open the chest and find a shiny gemstone! You're rich!")
        play_again()
    elif choice == '2':
        delay_print("You decide not to open the chest and continue your journey.")
        delay_print("You come across a river. What do you do?")
        delay_print("1. Attempt to swim across")
        delay_print("2. Look for a bridge")

        choice = input("Enter your choice (1/2): ")

        if choice == '1':
            delay_print("You try to swim across the river but get swept away by the strong current.")
            game_over()
        elif choice == '2':
            delay_print("You find a bridge and safely cross the river.")
            game_win()
        else:
            delay_print("Invalid choice. Please enter '1' or '2'.")
            left_path()
    else:
        delay_print("Invalid choice. Please enter '1' or '2'.")
        left_path()

def right_path():
    delay_print("You chose the right path and walk deeper into the forest.")
    delay_print("You encounter a ferocious bear!")
    delay_print("What will you do?")
    delay_print("1. Fight the bear")
    delay_print("2. Run away")

    choice = input("Enter your choice (1/2): ")

    if choice == '1':
        delay_print("You bravely fight the bear but unfortunately, it's too strong.")
        game_over()
    elif choice == '2':
        delay_print("You wisely decide to run away from the bear.")
        delay_print("After running for a while, you reach a clearing with a beautiful waterfall.")
        game_win()
    else:
        delay_print("Invalid choice. Please enter '1' or '2'.")
        right_path()

def game_win():
    delay_print("Congratulations! You have successfully reached the beautiful waterfall and won the game.")
    play_again()

def game_over():
    delay_print("Game over. You have failed in your adventure.")
    play_again()

def play_again():
    delay_print("Do you want to play again?")
    choice = input("Enter 'yes' or 'no': ").lower()
    if choice == 'yes':
        game_start()
    elif choice == 'no':
        delay_print("Thank you for playing!")
    else:
        delay_print("Invalid choice. Please enter 'yes' or 'no'.")
        play_again()

if __name__ == "__main__":
    game_start()
