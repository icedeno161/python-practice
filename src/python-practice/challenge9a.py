numbers = []

while True:
    num = input("Enter a number(or enter 'done'): ")

    if num == "done":
        break

    try:
        num = int(num)
    except ValueError:
        print("Please enter a valid integer or 'done'.")
        continue

    numbers.append(num)

if numbers:
    total = sum(numbers)
    print(F'the numbers you entered are: {numbers}')
    print(f'the sum of the numbers is: {total}')
    print(f'the average of the numbers is: {total/len(numbers)}')
else:
    print("No numbers were entered.")
