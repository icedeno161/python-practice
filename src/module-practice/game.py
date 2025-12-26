import random
from .utils import ask_positive_int

def play(max_attempts: int = 5) -> None:
    max_number = ask_positive_int("Enter the maximum number for the guessing range: ")
    secret_number = random.randint(1, max_number)
    attempts = 0

    print(f"I'm thinking of a number between 1 and {max_number}. You have {max_attempts} attempts to guess it!")

    while attempts < max_attempts:
        guess = ask_positive_int("Take a guess: ")
        attempts += 1

        if guess < secret_number:
            print("Too low!")
        elif guess > secret_number:
            print("Too high!")
        else:
            print(f"🎉 Correct! You guessed it in {attempts} attempts.")
            return

    print(f"Out of attempts! The number was {secret_number}.")
