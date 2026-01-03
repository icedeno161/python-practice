import pytest
from guessing_game.game import GuessingGame

def test_guess_too_low():
    game = GuessingGame(max_attempts=5, max_number=10)
    game.secret_number = 5

    result = game.make_guess(3)

    assert result == "Too low!"
    assert game.attempts == 1
