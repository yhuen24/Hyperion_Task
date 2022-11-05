# ask for user input
price = float(input("Enter package price: "))
distance = float(input("Enter total delivery distance in kms: "))
air_price = 0
insurance_price = 0
gift_price = 0
priority_price = 0
# ask if Air or Freight
air = input("Air or Freight: ")
# change air_price according to user input
if air.lower() == "air":
    air_price = 0.36
elif air.lower() == "freight":
    air_price = 0.25

# ask type of insurance
insurance = input("Full insurance or limited insurance: ")
# change insurance_price according to user input
if insurance.lower() == "full insurance":
    insurance_price = 50
elif insurance.lower() == "limited insurance":
    insurance_price = 25

# ask if gift or not
gift = input("Gift or no gift: ")
# change gift_price according to user input
if gift.lower() == "gift":
    gift_price = 15
elif gift.lower() == "no gift":
    gift_price = 10

# ask if priority or standard delivery
priority = input("priority or standard delivery: ")
if priority.lower() == "priority":
    priority_price = 100
elif priority.lower() == "standard delivery":
    priority_price = 20

total = (air_price * distance) + price + gift_price + priority_price + insurance_price
print(total)
