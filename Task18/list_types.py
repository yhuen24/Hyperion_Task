friends_names = ["Elon Musk", "Bill Gates", "Mark Zuckerberg"]
print(friends_names[0])  # access first element
print(friends_names[-1])  # access last element
print(len(friends_names))  # length of list
friends_ages = [40, 50, 30]

# prints the name and age
for i in range(len(friends_names)):
    print(f"{friends_names[i]} is {friends_ages[i]} years old.")
