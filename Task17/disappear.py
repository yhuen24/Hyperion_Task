sentence = input("Enter a sentence: ")
remove_character = input("Which character would you like to disappear: ")
new_sentence = ""
for ch in sentence:
    if ch not in list(remove_character):
        new_sentence += ch
print(new_sentence)
