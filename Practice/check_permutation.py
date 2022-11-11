# Given two strings, write a method to decide if one is a permutation of the other.
def check_permutation(str1, str2):
    flag = 0
    hashmap1 = {}
    hashmap2 = {}
    if len(str1) != len(str2):
        return f"{str2} is not a permutation of {str1}"
    else:
        for ch in str1:  # populates hashmap 1
            if ch not in hashmap1:
                hashmap1[ch] = 1
            else:
                hashmap1[ch] += 1

        for ch in str2:  # populates hashmap 2
            if ch not in hashmap2:
                hashmap2[ch] = 1
            else:
                hashmap2[ch] += 1
        # check if key exist in both hashmap then compare their value if they are the same
        for key in hashmap1:
            if key in hashmap2:
                if hashmap1[key] == hashmap2[key]:
                    flag = 1
            else:
                flag = 0

        # check flag
        if flag == 1:
            return f"{str2} is a permutation of {str1}"
        else:
            return f"{str2} is not a permutation of {str1}"


string_input1 = input("Enter 1st string: ")
string_input2 = input("Enter 2nd string: ")
result = check_permutation(string_input1, string_input2)
print(result)