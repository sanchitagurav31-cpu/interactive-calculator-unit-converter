
import random
from collections import Counter
import string

def number_guessing_game():
    number = random.randint(1, 100)
    attempts = 0
    score = 100

    print("\n--- Number Guessing Game ---")
    print("Guess a number between 1 and 100")

    while True:
        try:
            guess = int(input("Enter your guess: "))
        except ValueError:
            print("Please enter a valid number!")
            continue

        if guess < 1 or guess > 100:
            print("Enter a number between 1 and 100!")
            continue

        attempts += 1

        if guess < number:
            print("Too low! Try again.")
        elif guess > number:
            print("Too high! Try again.")
        else:
            score = max(100 - (attempts - 1) * 10, 10)
            print("Correct! You won!")
            print("Attempts:", attempts)
            print("Your score:", score)
            break

def word_counter():
    print("\n--- Word Counter ---")
    filename = input("Enter text file name: ")

    try:
        with open(filename, "r", encoding="utf-8") as file:
            text = file.read().lower()

        words = text.translate(
            str.maketrans("", "", string.punctuation)
        ).split()

        print("Total words:", len(words))
        print("Word frequency:")

        for word, count in Counter(words).most_common():
            print(word, ":", count)

    except FileNotFoundError:
        print("File not found! Check the file name.")

while True:
    print("\n1. Number Guessing Game")
    print("2. Word Counter")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        number_guessing_game()
    elif choice == "2":
        word_counter()
    elif choice == "3":
        print("Thank you!")
        break
    else:
        print("Invalid choice! Try again.")
