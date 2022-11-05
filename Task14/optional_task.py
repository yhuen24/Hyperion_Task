# Makes an infinite loop that only stop when user inputs less than or equal to 100
while True:
    num = int(input("Enter a number less than or equal to 100: "))
    if num <= 100:
        break

if num % 2 == 0:  # divides num by 2 to check if its even
    num *= 2
else:
    num *= 3
print(num)
