weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in m: "))
# BMI = (weight) / (Height) (Height)
bmi = weight / (height * height)

if bmi >= 30:
    print(f"Your bmi is {bmi}")
    print("Obese")
elif bmi >= 25:
    print(f"Your bmi is {bmi}")
    print("Overweight")
elif bmi >= 18.5:
    print(f"Your bmi is {bmi}")
    print("Normal")
else:
    print(f"Your bmi is {bmi}")
    print("Underweight")
