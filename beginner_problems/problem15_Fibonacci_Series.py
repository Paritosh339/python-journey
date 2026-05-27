#Add problem15 fibonacci series
#Print fibonacci series

number = int(input("Please enter your number: "))

a = 0
b = 1

for i in range(number):
    print(a, end=" ")
    next = a + b
    a = b
    b = next