# Problem 5 - Find the Largest Number
# Takes 5 numbers from user one by one and prints the largest
# Without using max() built-in function

list1 = []

for num in range(1, 6):
    numbers = input(f"Please enter your number no {num}: ")
    list1.append(numbers)

largest = list1[0]

for num in list1:
    if num > largest:
        largest = num

print(f"Your greatest number is: {largest}")