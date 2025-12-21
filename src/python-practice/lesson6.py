def count_to_n(n):
    for i in range(1, n + 1):
        print(i)

count_to_n(5)

def sum_numbers(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total

result = sum_numbers(5)
print(result)  # 15

def ask_for_number():
    while True:
        value = input("Enter a number: ")
        if value.isdigit():
            return int(value)
        else:
            print("Invalid input, try again.")

number = ask_for_number()
print("You entered:", number)

def is_even(n):
    return n % 2 == 0

for i in range(1, 11):
    if is_even(i):
        print(i, "is even")
    else:
        print(i, "is odd")

def find_first_multiple_of_7(limit):
    for i in range(1, limit + 1):
        if i % 7 == 0:
            return i
    return None

print(find_first_multiple_of_7(20))
