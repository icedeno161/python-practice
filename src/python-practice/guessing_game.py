import random

def play_game():

    max_number = input("Enter the maximum number for the guessing range: ")

    if not max_number.isdigit():
        print("Please enter a valid positive integer.")
        return
    max_number = int(max_number)
    secret_number = random.randint(1, max_number)
    attempts = 0

    print(f"I'm thinking of a number between 1 and {max_number}. You have 5 attempts to guess it!")

    while attempts < 5:
        guess = input("Take a guess: ")
        
        if not guess.isdigit():
            print("Please enter a valid number.")
            continue

        guess = int(guess)
        attempts += 1

        if guess < secret_number:
            print("Too low!")
        elif guess > secret_number:
            print("Too high!")
        else:
            print(f"🎉 Correct! You guessed it in {attempts} attempts.")
            break

    if attempts == 5 and guess != secret_number:
        print(f"Sorry, you've used all your attempts. The number was {secret_number}.")

while True:
    play_game()
    play_again = input("play again? (yes/no): ").strip().lower()

    if play_again != 'yes':
        break