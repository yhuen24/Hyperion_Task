# importing math to call pi
import math
shape = input("Enter building shape (square, rectangular, round): ")
if shape.lower() == "square":
    square_side = float(input("Enter side length: "))
    # area of square is side * side or side^2
    square_area = square_side * square_side
    print(f"The are of {shape.lower()} is {square_area}")

elif shape.lower() == "rectangular":
    length = float(input("Enter length: "))
    width = float(input("Enter width: "))
    # area of rectangle is Length * Width
    rectangular_area = length * width
    print(f"The are of {shape.lower()} is {rectangular_area}")

elif shape.lower() == "round":
    radius = float(input("Enter radius: "))
    # area of circle is pi * (radius * radius)
    round_area = math.pi * (radius * radius)
    # rounds to 2 decimal places
    print(f"The are of {shape.lower()} is {round(round_area, 2)}")

# handles any invalid input
else:
    print(shape)
    print("Please enter a valid input")