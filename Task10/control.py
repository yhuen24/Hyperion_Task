age = int(input("Enter your age: "))

# Checks if user is over 18
if age >= 18:
    print("You are old enough")
# Checks if user is over 16 and under 18 range
elif 16 < age < 18:  # the same as saying (age > 16 and age < 18)
    print("Almost there")
# any input below 17 activates this block
else:
    print("You're just too young!")
