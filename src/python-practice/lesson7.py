def ask_positive_int(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value <= 0:
                print("Please enter a number greater than 0.")
                continue
            return value
        except ValueError:
            print("Please enter a valid whole number.")

max_number = ask_positive_int("Enter the maximum number for the guessing range: ")
guess = ask_positive_int("Take a guess: ")