def calculator(num1, operator, num2):
    if operator == "+":
        return num1 + num2
    elif operator == "-":
        return num1 - num2
    elif operator == "*":
        return num1 * num2
    elif operator == "/" and num2 == 0:
        return("Cannot divide by zero")
    else:
        return num1 / num2

print("welcome to a very basic calculator system")
num1 = int(input("Please enter your number 1: "))
operator = input("Please enter your operator: ")
num2 = int(input("Please enter your number 2: "))

print(f"your answer is {(calculator(num1, operator, num2))}")
