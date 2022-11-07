num = int(input("Enter a number: ")  # parenthesis not close properly which causes syntax error

if num % 2 == 0;  # semicolon instead of colon making a syntax error
    print(f"{num} is odd")  # odd and even is switched making a logical error
else:
    # adding [0] makes it an iterable object which causes a runtime error due to TypeError
    print(f"{num[0]} is even")