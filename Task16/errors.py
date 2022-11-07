# This example program is meant to demonstrate errors.

# There are some errors in this program, try run the program by pressing F5.
# Now look at the error messages and find and fix the errors.

print("Welcome to the error program")  # syntax error missing parenthesis
print("\n")  # syntax error missing parenthesis

# syntax error, wrong indentation
ageStr = "24"  # I'm 24 years old. (runtime error wrong string)
age = int(ageStr)
print("I'm " + str(age) + " years old.")  # syntax error, cast int to string before concatenation
three = "3"
# syntax error, wrong indentation
# logical error on formula, half year missing
answerYears = age + int(three) + 0.5  # syntax error, cast three to int

print("The total number of years:" + str(answerYears))  # syntax error missing parenthesis
answerMonths = answerYears * 12  # Runtime error, there is no variable named "answer"
# syntax error, cast answerMonths to string before concatenation
print("In 3 years and 6 months, I'll be " + str(answerMonths) + " months old")  # syntax error missing parenthesis

# HINT, 330 months is the correct answer
