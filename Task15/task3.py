# create a while loop that will display countdown from 20 to 0
countdown = 20
while countdown >= 0:
    print(countdown)
    countdown -= 1
print("=======================")  # printing this line to separate the steps

# Create a loop (any) that will display all even numbers between 1 and 2
for i in range(1, 21):
    if i % 2 == 0:
        print(i)
print("=======================")  # printing this line to separate the steps

# Create a loop that will produce the following output:
for i in range(1, 6):
    print("*" * i)  # multiplies the number of * by i
print("=======================")  # printing this line to separate the steps

# Write the code to compute the greatest common divisor (GCD) or highest common factor of 2 positive integers
num1 = int(input("Enter num1: "))
num2 = int(input("Enter num2: "))
hcf = 1  # highest common factor default by 1
# find out which is greater in 2 input
greater_num = max(num1, num2)
# makes sure it loops using greater num
for i in range(1, greater_num):
    if num1 % i == 0 and num2 % i == 0:
        hcf = i
print(hcf)
