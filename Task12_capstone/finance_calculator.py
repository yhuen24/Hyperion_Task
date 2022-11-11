import math

print("Choose either 'investment' or 'bond' from the menu below to proceed: ")
print("investment \t-\t to calculate the amount of interest you'll earn on your investment")
print("bond \t-\t to calculate te amount you''' have to pay on a home loan\n")
choice = input()

# make choice all lower case so that capitalization don't matter
if choice.lower() == "investment":
    result = 0
    deposit_amount = float(input("Enter deposit amount: "))
    interest_rate = float(input("Enter interest rate percentage: "))
    year_number = float(input("Enter number of years: "))
    interest_type = input("Simple or Compound interest? : ")
    # make interest_type all lower case so that capitalization don't matter
    if interest_type.lower() == "simple":
        # A = P (1 + r * t)
        result = deposit_amount * (1 + (interest_rate * year_number))
    elif interest_type.lower() == "compound":
        # A = P (1 + r) ^ t
        result = deposit_amount * math.pow((1 + interest_rate), year_number)
    # display result rounded to 2 decimal places
    print(round(result, 2))
elif choice.lower() == "bond":
    house_value = float(input("Enter house value: "))
    interest_rate = float(input("Enter interest rate percentage: "))
    month_number = float(input("Enter number of months: "))
    # x = (i * P) / (1 - (1 + i) ^ (-n)
    i = interest_rate / 12  # i is the monthly interest rate, calculated by dividing the annual interest rate by 12
    result = (i * house_value) / (1 - math.pow(1 + i, -month_number))
    # display result rounded to 2 decimal places
    print(round(result, 2))
