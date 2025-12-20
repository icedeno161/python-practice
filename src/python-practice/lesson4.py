for i in range(5):
    print("Loop number:", i)

fruits = ["apple", "banana", "orange"]

for fruit in fruits:
    print(fruit)

count = 1

while count <= 5:
    print("Count is:", count)
    count += 1

for i in range(10):
    if i == 5:
        break
    print(i)

for i in range(5):
    if i == 2:
        continue
    print(i)
