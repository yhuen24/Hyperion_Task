counter = 0

# Creates an infinite loop that only stop when user inputs "Stop"
while True:
    name = input("Enter student name: ")
    # makes name lower case so that capitalization don't matter
    if name.lower() == "stop":
        print(counter)
        break
    counter += 1  # add 1 to counter for every name inputted
