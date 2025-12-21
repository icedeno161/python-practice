def ask_float(prompt):
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("Please enter a valid decimal number.")

price = ask_float("Enter the price: ")
print("You entered:", price)