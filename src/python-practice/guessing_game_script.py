import random


def safe_input(prompt):
    """Return user input or None if the user triggers EOF/interrupt."""
    try:
        return input(prompt)
    except (EOFError, KeyboardInterrupt):
        print("\nExiting game.")
        return None


def get_positive_int(prompt):
    """Prompt until the user provides a positive integer or exits."""
    while True:
        user_input = safe_input(prompt)
        if user_input is None:
            return None

        user_input = user_input.strip()
        if not user_input.isdigit():
            print("Please enter a valid positive integer.")
            continue

        value = int(user_input)
        if value <= 0:
            print("Please enter a number greater than zero.")
            continue

        return value


def play_game():
    max_number = get_positive_int("Enter the maximum number for the guessing range: ")
    if max_number is None:
        return False

    secret_number = random.randint(1, max_number)
    attempts = 0

    print(f"I'm thinking of a number between 1 and {max_number}. You have 5 attempts to guess it!")

    while attempts < 5:
        guess = get_positive_int("Take a guess: ")
        if guess is None:
            return False

        attempts += 1

        if guess < secret_number:
            print("Too low!")
        elif guess > secret_number:
            print("Too high!")
        else:
            print(f"🎉 Correct! You guessed it in {attempts} attempts.")
            return True

    print(f"Sorry, you've used all your attempts. The number was {secret_number}.")
    return True


while True:
    finished = play_game()
    if not finished:
        break

    play_again = safe_input("play again? (yes/no): ")
    if play_again is None or play_again.strip().lower() != "yes":
        break