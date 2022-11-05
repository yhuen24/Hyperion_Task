str_manip = input("Enter a  sentence: ")
n = len(str_manip)
last_letter = str_manip[-1]
new_str = str_manip.replace(last_letter, "@")
print(str_manip[::-1][:3])
word = str_manip[0:3] + str_manip[-2:]
print(word)