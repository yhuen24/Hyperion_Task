# FIzz BUZZ challenge
# pylint: disable-all

for i in range(1, 101):
    if i % 3 == 0:
        print("Fizz", end="")
    if i % 5 == 0:
        print("Buzz", end="")
    print()