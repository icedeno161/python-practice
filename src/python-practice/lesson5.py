def greet(name="Guest"):
    print(f"Hello, {name}!")

greet("Alex")
greet("Sam")
greet()

def add(a, b):
    return a + b

result = add(3, 5)
print(result)

def check_even(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"

print(check_even(4))
print(check_even(7))
