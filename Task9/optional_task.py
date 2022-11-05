employee_type = input("Salesperson or Manager?: ")
wage = 0
hourly_rate = 40  # hourly rate for managers
commission = 0.08  # equivalent to 8% in decimals
fixed_salary = 2000  # R200 base pay for salesman
# check if user is salesperson
if employee_type.lower() == "salesperson":
    gross_sale = float(input("Enter your gross sale for the month: "))
    # (Gross sale x 8%) + R2000
    wage = (gross_sale * commission) + fixed_salary

# check if user is manager
elif employee_type.lower() == "manager":
    num_hours = float(input("Enter your number of hours worked for the month: "))
    wage = num_hours * hourly_rate

print(wage)