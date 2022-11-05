num = int(input("Enter a number: "))
# loops from 1 to num
for i in range(1, num + 1):
    result = num * i
    print(f"{num} x {i} = {result}")