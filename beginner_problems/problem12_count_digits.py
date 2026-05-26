#Add problem12 count digits

number = int(input("Please enter your number: "))

count = 0

while number > 0 :
    number = number // 10
    count += 1

print(f"Total digits: {count}")

