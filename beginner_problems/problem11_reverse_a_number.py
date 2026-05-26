#problem11 reverse a number
# No converting to string allowed!

number = int(input("Please enter your number: "))
reversed_number = 0

while number > 0:
    last_digit = number % 10
    reversed_number = reversed_number * 10 + last_digit
    number = number // 10

print(reversed_number)
