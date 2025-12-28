import random
from dataclasses import dataclass, field

from .utils import ask_positive_int


@dataclass
class GuessingGame:
    max_attempts: int = 5
    max_number: int = 10
    secret_number: int = field(init=False)
    attempts: int = field(default=0, init=False)

    def __post_init__(self) -> None:
        # Create a secret number after max_number is known
        self.secret_number = random.randint(1, self.max_number)

    def reset(self, max_number: int | None = None) -> None:
        """Reset the game state (new secret number, attempts back to 0)."""
        if max_number is not None:
            self.max_number = max_number
        self.attempts = 0
        self.secret_number = random.randint(1, self.max_number)

    def make_guess(self, guess: int) -> str:
        """Process one guess and return feedback."""
        self.attempts += 1

        if guess < self.secret_number:
            return "Too low!"
        if guess > self.secret_number:
            return "Too high!"
        return "Correct!"

    def play(self) -> None:
        """Run one full game round."""
        print(
            f"I'm thinking of a number between 1 and {self.max_number}. "
            f"You have {self.max_attempts} attempts!"
        )

        while self.attempts < self.max_attempts:
            guess = ask_positive_int("Take a guess: ")
            result = self.make_guess(guess)

            if result == "Correct!":
                print(f"🎉 Correct! You guessed it in {self.attempts} attempts.")
                return
            else:
                print(result)

        print(f"Out of attempts! The number was {self.secret_number}.")
