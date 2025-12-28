import json
from pathlib import Path

# Store user data alongside this script so location is predictable
USER_FILE = Path(__file__).resolve().parent / "user.json"


def load_saved_name() -> str | None:
    """Return stored name or None if the file is missing or invalid."""
    if not USER_FILE.exists():
        return None

    try:
        with open(USER_FILE, "r", encoding="utf-8") as file:
            data = json.load(file)
        name = data["name"]
        if not isinstance(name, str) or not name.strip():
            return None
        return name.strip().title()
    except (OSError, json.JSONDecodeError, KeyError):
        # File not readable or malformed JSON; treat as no saved name
        return None


def prompt_for_name() -> str:
    """Ask until a non-empty name is provided."""
    while True:
        name = input("Enter your name: ").strip()
        if name:
            return name.title()
        print("Please enter a non-empty name.")


def save_name(name: str) -> None:
    """Persist the user's name, handling disk errors gracefully."""
    try:
        with open(USER_FILE, "w", encoding="utf-8") as file:
            json.dump({"name": name}, file)
    except OSError as err:
        print(f"Couldn't save your name ({err}).")


def main() -> None:
    saved_name = load_saved_name()
    if saved_name:
        print(f"Welcome back, {saved_name}!")
        return

    name = prompt_for_name()
    save_name(name)
    print(f"Hello, {name}! Your name has been saved.")


if __name__ == "__main__":
    main()
