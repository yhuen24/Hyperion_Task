word = input("Enter a string: ")
alternative_word = ""  # empty string that I will populate with alternating characters case
lower_alternative_word = ""  # empty string that I will populate with alternating characters case
for i in range(len(word)):  # loops through the string
    if i % 2 == 0:
        alternative_word += word[i].upper()
        lower_alternative_word += word[i].lower()
    else:
        alternative_word += word[i].lower()
        lower_alternative_word += word[i].upper()
print(alternative_word)
print(lower_alternative_word)


