# This example program is meant to demonstrate errors.
 
# There are some errors in this program, try run the program by pressing F5.
# Now look at the error messages and find and fix the errors.

animal = "Lion"  # syntax error, needed "" for strings
animal_type = "cub"
number_of_teeth = 16

# runtime error, missing f for f string formatting
# logical error, number_of_teeth swap places with cub
full_spec = f"This is a {animal}. It is a {animal_type} and it has {number_of_teeth} teeth"

print(full_spec)  # syntax error parenthesis missing

