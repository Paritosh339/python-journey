def is_prime(number):
    for i in range(2, number):
        if number % i == 0:
            return("not a prime")

    return("a prime")

number = int(input("Please enter your number: "))

print(f"{number} is {is_prime(number)} number")