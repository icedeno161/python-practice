scores = {}

while True:
    name = input("Player name (or 'quit'): ").strip()
    if name == "quit":
        break

    score = int(input("Score: "))
    scores[name] = score

print("Final scores:")
for name, score in scores.items():
    print(name, ":", score)
