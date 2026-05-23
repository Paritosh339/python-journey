print("Welcome to string reversal system")
string = input("Please enter your string: ")

result = ""

for ch in string :
    result = ch + result

print(result)