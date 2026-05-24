def find_max(num1, num2, num3):
    numbers = [num1, num2, num3]
    

    largest = numbers[0]

    for i in numbers:
        if i > largest:
            largest = i
    return largest


num1 = int(input("Please enter your 1st number: "))
num2 = int(input("Please enter your 2nd number: "))
num3 = int(input("Please enter your 3rd number: "))


print(f"Your greatest number is: {find_max(num1, num2, num3)}")


    