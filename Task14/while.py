# Makes an infinite loop that only stop when user inputs -1
running_sum = 0
num_count = 0
while True:
    num = int(input("Enter num: "))
    if num == -1:
        average = running_sum / num_count
        print(f"Average is: {average}")
        break
    running_sum += num  # add num to running sum
    num_count += 1  # add 1 to num_count
