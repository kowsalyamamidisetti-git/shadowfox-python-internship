#python
import random

# List of words for the game
words = ["python", "apple", "cricket", "computer"]

# Select a random word
secret_word = random.choice(words)
guessed_letters = []
attempts = 6

print("Welcome to Hangman!")

while attempts > 0:
    display_word = ""

    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter
        else:
            display_word += "_"

    print("\nWord:", display_word)
    print("Attempts left:", attempts)

    if display_word == secret_word:
        print("Congratulations! You won!")
        break

    guess = input("Guess a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter one letter.")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter!")
        continue

    guessed_letters.append(guess)

    if guess in secret_word:
        print("Correct guess!")
    else:
        print("Wrong guess!")
        attempts -= 1

if attempts == 0:
    print("Game over! The word was:", secret_word)
