swimming_time = float(input("Enter swimming time: "))
cycling_time = float(input("Enter cycling time: "))
running_time = float(input("Enter running time: "))
# calculates total time by adding all time inputs
total_time = swimming_time + cycling_time + running_time
print(f"Total time: {total_time}")

if total_time <= 100:
    print("Provincial Colours")

# check if total_time is within range of 101 to 105
elif 100 < total_time <= 105:
    print("Provincial Half Colours")

# check if total_time is within range of 105 to 110
elif 105 < total_time <= 110:
    print("Provincial Scroll")

else:
    print("No award")
