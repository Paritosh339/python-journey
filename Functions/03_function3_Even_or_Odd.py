#function3 Even or Odd

def OddEven(number):
    if number % 2 == 0:
        return("Even")
    else:
        return("Odd")

number = int(input("Please enter your number: "))

print(f"Your number is {OddEven(number)}")