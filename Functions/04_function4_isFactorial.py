#function8 check factorial

def isFactorial(number):
    total = 1
    for i in range(1, number + 1):
       total = total * i
    return total
    
number = int(input("Please enter your number: "))

print(f"Factorial of {number} is {isFactorial(number)}")
