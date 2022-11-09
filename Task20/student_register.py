num = int(input("How many number of student: "))
id_list = []
for i in range(num):
    id_input = input("Enter student ID: ")
    id_list.append(id_input)  # adds id_input to the empty list

with open('reg_form.txt', 'w+') as f:
    for i in id_list:  # write id for every id in id_list
        f.writelines(f"{i} \n")

    f.write("\n-----------")  # prints the line for signature
