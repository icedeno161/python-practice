from .game import GuessingGame
from .utils import ask_positive_int


def main() -> None:
    while True:
        max_number = ask_positive_int("Enter the maximum number for the guessing range: ")
        game = GuessingGame(max_attempts=5, max_number=max_number)
        game.play()

        again = input("Play again? (yes/no): ").strip().lower()
        if again != "yes":
            break


if __name__ == "__main__":
    main()
