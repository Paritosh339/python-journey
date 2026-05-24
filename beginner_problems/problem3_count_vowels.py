print("Welcome to vowel counter system")

sentence = input("Please enter your sentence:").lower()

total = 0

for ch in sentence:
    if ch in "aeiou" :
        total += 1

print("Total number of vowels are :",total)