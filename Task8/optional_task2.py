# Default value as False
temperature = False
weekend = False
sunny = False
# empty string variable to be appended when condition checks out
shirt = ""
short = ""
cap = ""

temperature_input = input("Is the temperature greater than 20 degrees?: ")
# check if user input yes, meaning temp is 20 degree above
if temperature_input == "yes":
    temperature = True
    shirt += "short-sleeved shirt"
elif temperature_input == "no":
    shirt += "long-sleeved shirt"

weekend_input = input("Is it weekend?: ")
# check is user input yes, meaning it is weekend
if weekend_input == "yes":
    weekend = True
    short += "shorts"
elif weekend_input == "no":
    short += "jeans"

sunny_input = input("Is it sunny?: ")
# check is user input yes, meaning it is sunny
if sunny_input == "yes":
    sunny = True
    cap += "cap"
elif sunny_input == "no":
    cap += "raincoat"

# display the strings appended
print(f"You should wear {shirt}, {short} and {cap}")


