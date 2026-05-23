# Problem 4 - FizzBuzz
# Print numbers from 1 to 50
# Print "Fizz" for multiples of 3
# Print "Buzz" for multiples of 5
# Print "FizzBuzz" for multiples of both 3 and 5

for i in range(1, 51):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)