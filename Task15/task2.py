start_year = int(input("What year do you want to start with?    "))
num = int(input("How many years do you want to check?   "))

for i in range(num):
    if start_year % 4 == 0:
        print(f"{start_year} is a leap year")
    else:
        print(f"{start_year} isn't a leap year")
    start_year += 1