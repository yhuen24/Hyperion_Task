# Implement an algorithm to determine if a string has all unique characters.
# What if you cannot use additional data structures?
def check_is_unique(my_string):
    ch_set = set()
    for ch in my_string:
        if ch not in ch_set:
            ch_set.add(ch)
        else:
            return "Your string has duplicate characters"
    return "Your string has all unique characters"

input_string = input("Enter a string: ")
print(check_is_unique(input_string))
