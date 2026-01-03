import unittest
from guessing_game.game import GuessingGame


class TestGuessingGame(unittest.TestCase):

    def test_correct_guess(self):
        game = GuessingGame(max_attempts=5, max_number=10)

        # Force known state
        game.secret_number = 5

        result = game.make_guess(5)

        self.assertEqual(result, "Correct!")
        self.assertEqual(game.attempts, 1)

    def test_guess_too_low(self):
        game = GuessingGame(max_attempts=5, max_number=10)
        game.secret_number = 5

        result = game.make_guess(3)

        self.assertEqual(result, "Too low!")
        self.assertEqual(game.attempts, 1)

    def test_guess_too_high(self):
        game = GuessingGame(max_attempts=5, max_number=10)
        game.secret_number = 5

        result = game.make_guess(8)

        self.assertEqual(result, "Too high!")
        self.assertEqual(game.attempts, 1)


if __name__ == "__main__":
    unittest.main()
