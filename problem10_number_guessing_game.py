#Number guessing game between 1 to 100

import random

number = random.randint(1, 100)

attempts = 0
first_guess = True

while True:
    if first_guess:
        guess = int(input("Guess a number between 1 to 100: "))
        first_guess = False
    else:
        guess = int(input("Try again: "))
    
    attempts += 1
    
    if guess > number:
        print("Too high!")
    elif guess < number:
        print("Too low!")
    else:
        print(f"Correct! You got it in {attempts} attempts!")
        break