#Add problem13 Sum of Even and Odd Numbers


numbers = [5, 6, 9, 76, 43, 55, 76, 12, 33]

even_numbers = []
odd_numbers = []

for i in numbers :
    if i % 2 == 0:
        even_numbers.append(i)
    else :
        odd_numbers.append(i)

print(f"Sum of even numbers: {sum(even_numbers)}\nSum of odd numbers: {sum(odd_numbers)}")