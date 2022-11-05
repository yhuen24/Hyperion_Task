num1 = 444
num2 = 14
num3 = 44

# check if num1 is greater than num2 if not then num2 is greater
if num1 > num2:
    print(num1)
else:
    print(num2)

# divides num1 to 2, if there is no remainder it means num1 is even
if num1 % 2 == 0:
    print(f"{num1} is even")
else:
    print(f"{num1} is odd")

# checks if num1 is greater than num2 and num3
if num1 > num2 and num1 > num3:
    # checks greater from num2 and num3
    if num2 > num3:
        print(f"sorted values: {num1}, {num2}, {num3}")
    else:
        print(f"sorted values: {num1}, {num3}, {num2}")
# checks if num2 is greater than num1 and num3
elif num2 > num1 and num2 > num3:
    # checks if num1 is greater than num3
    if num1 > num3:
        print(f"sorted values: {num2}, {num1}, {num3}")
    else:
        print(f"sorted values: {num2}, {num3}, {num1}")
# if code goes here it means num3 is the greatest num
else:
    # checks if num1 is greater than num2
    if num1 > num2:
        print(f"sorted values: {num3}, {num1}, {num2}")
    else:
        print(f"sorted values: {num3}, {num2}, {num1}")