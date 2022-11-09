# file handler for numbers1.txt
with open('numbers1.txt', 'r+') as f:
    data = f.read()
    num1_list = data.split()

# file handler for numbers2.txt
with open('numbers2.txt', 'r+') as f2:
    data2 = f2.read()
    num2_list = data2.split()

combined_num = []  # this will store the integer version of the number list
# casting num1_list to int
for i in range(len(num1_list)):
    combined_num.append(int(num1_list[i]))

# casting num2_list to int
for i in range(len(num2_list)):
    combined_num.append(int(num2_list[i]))

sorted_combined_num = sorted(combined_num)  # sort the combined num ascending order
with open('all_numbers.txt', 'w+') as writer:
    for i in sorted_combined_num:
        writer.write(f"{str(i)} ")



