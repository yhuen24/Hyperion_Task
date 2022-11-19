string_input = input("Enter a string: ")
new_string = ""
for i in string_input:
    new_string = string_input.replace(" ", "%20")
print(new_string)
