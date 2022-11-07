name_list = []  # this list stores the wrong input
while True:
    name = input("Enter name: ")
    if name.lower() == "john":
        print(f"Incorrect names: {name_list}")
        break  # breaks the infinite loop
    else:
        name_list.append(name)  # add wrong input name to name_list
