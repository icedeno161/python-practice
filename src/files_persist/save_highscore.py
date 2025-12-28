import json
from pathlib import Path

SCORE_FILE = Path("high_score.json")

def save_score(score: int) -> None:
    with open(SCORE_FILE, "w") as file:
        json.dump({"high_score": score}, file)

def load_score() -> int:
    if SCORE_FILE.exists():
        with open(SCORE_FILE, "r") as file:
            return json.load(file)["high_score"]
    return 0

if __name__ == "__main__":
    current_high_score = load_score()
    print(f"Current High Score: {current_high_score}")
    new_score = int(input("Enter your new score: "))
    if new_score > current_high_score:
        save_score(new_score)
        print("New high score saved!")
    else:
        print("Score not high enough to save.")