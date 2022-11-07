sentence = input("Enter your sentence: ")
reverse_sentence = sentence[::-1]  # reversed the string using string slicing
palindrome = "Your word is not Palindrome"  # not palindrome by default
for i in range(len(sentence)):
    if sentence[i] == reverse_sentence[i]:
        palindrome = "Your word is Palindrome"
    else:
        palindrome = "Your word is not Palindrome"
        break  # break the loop if it found a not matching case]
print(palindrome)
