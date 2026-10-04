# Number Guessing Game

import random

while True:
    number = random.randint(1, 100)
    attempts = 0

    print("\nI have selected a number between 1 and 100.")
    print("Try to guess it!")

    while True:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1

            if guess < number:
                print("Too low! Try again.")

            elif guess > number:
                print("Too high! Try again.")

            else:
                print("Congratulations! You guessed the number!")
                print("Number of attempts:", attempts)
                break

        except ValueError:
            print("Please enter a valid number.")

    play_again = input("\nDo you want to play again? (yes/no): ")

    if play_again.lower() != "yes":
        print("Thanks for playing!")
        break