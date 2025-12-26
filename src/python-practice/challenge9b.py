# Collects user-entered names and ages, reporting those over 18.
ages = {}

while True:
    name = input("Enter name: (enter 'done' to finish): ")
    if name == "done":
        break
    if not name:
        print("Name cannot be empty. Try again.")
        continue

    try:
        age = int(input("Enter age: "))
        if age < 0:
            print("Age cannot be negative. Try again.")
            continue
    except ValueError:
        print("Please enter a valid number for age.")
        continue

    ages[name] = age  # Store valid name-age pairs.

over_18 = [name for name, age in ages.items() if age > 18]  # Filter adults.

if over_18:
    print(f"These are the names who are over 18 years old: {', '.join(over_18)}")
else:
    print("No one over 18 was entered.")
