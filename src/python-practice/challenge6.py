def print_multiplication_table(n):
    for i in range(1, 11):
        print(f"{n} x {i} = {n * i}")   

table_number = int(input("Enter a number to print its multiplication table: "))
print_multiplication_table(table_number)