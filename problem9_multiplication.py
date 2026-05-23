#problem9_multiplication_table

number = int(input("Please enter your number: "))

for i in range(1, 11) :
    total = (number * i)
    print(f"{number} X {i} = {total}")
