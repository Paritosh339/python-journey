# Problem 6 - Palindrome Checker
# Takes a word from user and checks if it is a palindrome
# Without using [::-1] slicing

print("Welcome to palindrome checker: ")

string = input("Please input your string: ").lower()

result = ""
for i in string:
    result = i + result

if string == result:
    print("It is a palindrome")
else:
    print("It is not a palindrome")