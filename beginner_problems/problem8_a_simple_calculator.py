while True:
    num1 = input("Please enter your 1st number: ")
    if num1 == "quit":
        print("Goodbye!")
        break
    num1 = int(num1)
    
    operator = input("Please enter your operator: ")
    
    num2 = int(input("Please enter your 2nd number: "))

    if operator == "+":
        print(num1 + num2)
    elif operator == "-":
        print(num1 - num2)
    elif operator == "*" :
        print(num1 * num2)
    elif operator == "/" and num2 == 0:
      print("Can't divide by zero")
    elif operator == "/" :
        print(num1 / num2)
