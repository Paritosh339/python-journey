#problem 7 remove duplicates without using set()

print("Welcome to duplicate remove system")

numbers = [2, 5, 6, 7, 8, 4, 4, 5]

new_numbers = []

for num in numbers:
    if num not in new_numbers:
        new_numbers.append(num)

print(new_numbers)