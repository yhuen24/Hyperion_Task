# logical error that determines if a number is odd or even

num = int(input("Enter a number: "))

if num % 2 == 0:
    print(f"{num} is odd")  # num should be even
else:
    print(f"{num} is even")