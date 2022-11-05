name = input("Enter your full name: ")
# get the length of name
name_length = len(name)

# test the length of name
# name_length 0 means empty input
if name_length == 0:
    print("You haven't entered anything. Please enter your full name.")
elif name_length < 4:
    print("You have entered less than 4 characters. Please make sure that you have entered your name and surname.")
elif name_length > 25:
    print("You have entered more than 25 characters. Please make sure that you have only entered your name and surname.")#
else:
    print("Thank you for entering your name.")
