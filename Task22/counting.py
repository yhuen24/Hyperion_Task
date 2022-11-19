input_string = input("Enter a string: ")
ch_dict = {}  # empty character dictionary
for i in input_string:
    if i in ch_dict:
        ch_dict[i] += 1  # add 1 if character is already in the dictionary
    else:
        ch_dict[i] = 1  # add the character to the dictionary

print(ch_dict)
