tasks = []

while True:
    task = input("Enter a task (or 'quit'): ").strip().lower()

    if task == "quit":
        break

    tasks.append(task)

print("Your tasks:")
for task in tasks:
    print("-", task)
