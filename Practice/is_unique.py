# Implement an algorithm to determine if a string has all unique characters.
# What if you cannot use additional data structures?
def check_is_unique(my_string):
    flag = 0
    hashmap = {}
    for ch in my_string:
        if ch not in hashmap:
            hashmap[ch] = 1
        else:
            hashmap[ch] += 1
            flag = 1

    if flag == 1:
        for key in hashmap:
            if hashmap[key] > 1:
                print(f"There is {hashmap[key]} number of {key} in your string")
        return "Your string has duplicate characters"
    else:
        return "Your string has all unique characters"


input_string = input("Enter a string: ")
print(check_is_unique(input_string))
