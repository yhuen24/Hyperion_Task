num1 = int(input("Enter num1: "))
num2 = int(input("Enter num2: "))
print(f"Before swap: num1: {num1} num2: {num2}")
num1 = num1 + num2
num2 = num1 - num2
num1 = num1 - num2
print(f"After swap: num1: {num1} num2: {num2}")