import json
from pathlib import Path

STATS_FILE = Path(__file__).with_name("stats.json")

def load_stats() -> dict:
    """Load stats from stats.json. If missing/corrupt, return defaults."""
    default = {
        "games_played": 0,
        "wins": 0,
        "best_attempts": None,   # fewest attempts on a win
        "last_max_number": None,
    }

    if not STATS_FILE.exists():
        return default

    try:
        with open(STATS_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)

        # Merge with defaults so missing keys don't crash
        for k, v in default.items():
            data.setdefault(k, v)
        return data
    except (json.JSONDecodeError, OSError):
        return default

def save_stats(stats: dict) -> None:
    """Save stats to stats.json."""
    with open(STATS_FILE, "w", encoding="utf-8") as f:
        json.dump(stats, f, indent=4)

def ask_positive_int(prompt: str) -> int:
    while True:
        try:
            value = int(input(prompt))
            if value <= 0:
                print("Please enter a number greater than 0.")
                continue
            return value
        except ValueError:
            print("Please enter a valid whole number.")
