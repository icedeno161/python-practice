from .game import play

def main() -> None:
    while True:
        play()
        again = input("Play again? (yes/no): ").strip().lower()
        if again != "yes":
            break

if __name__ == "__main__":
    main()
