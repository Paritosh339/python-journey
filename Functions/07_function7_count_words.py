def count_words(sentence):
    new_list = sentence.split()

    count = 0

    for i in new_list:
        count += 1

    return count

sentence = input("Please enter your sentence: ")

print(f"Your total words are {count_words(sentence)}")