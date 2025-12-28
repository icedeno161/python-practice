from .game import GuessingGame
from .utils import ask_positive_int, load_stats, save_stats


def main() -> None:
    stats = load_stats()

    print("📊 Stats:")
    print(f"Games played: {stats['games_played']}")
    print(f"Wins: {stats['wins']}")
    print(f"Best attempts: {stats['best_attempts']}\n")

    while True:
        max_number = ask_positive_int("Enter the maximum number for the guessing range: ")
        game = GuessingGame(max_attempts=5, max_number=max_number)

        won, attempts_used = game.play()

        # Update stats
        stats["games_played"] += 1
        stats["last_max_number"] = max_number

        if won:
            stats["wins"] += 1
            best = stats["best_attempts"]
            if best is None or attempts_used < best:
                stats["best_attempts"] = attempts_used

        save_stats(stats)

        again = input("Play again? (yes/no): ").strip().lower()
        if again != "yes":
            break


if __name__ == "__main__":
    main()
