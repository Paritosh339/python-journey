data = input("Please enter you number:")

list = []
for digit in data:
    list.append(int(digit))

print(sum(list))