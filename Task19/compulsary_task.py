content = ""
birthdate = ""
number_list = ['1', '2', '3', '4', '5', '6', '7', '8', '9']  # list of numbers
with open('DOB.txt', 'r+') as f:
    for line in f:
        content += line
        for i in range(len(line)):  # loops through the line character by character
            if line[i] in number_list:  # check if character is a number
                for j in range(i, len(line)):  # store the following character to an empty string
                    birthdate += line[j]
                break  # break so that it does not store over and over

    print("Name")
    print(content)
    print("Birthdate")
    print(birthdate)
