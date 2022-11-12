# Given an array of integers that are out of order
# Determine the bounds if the smallest window that must be sorted in order for the entire array to be sorted
# Example: [3,7,5,6,9] return must be (1,3)

import math

n = int(input("Enter array size: "))
my_list = []
for i in range(n):
    elem = int(input("Enter element: "))
    my_list.append(elem)


def window(arr):
    size = len(arr)
    left = None
    right = None
    min_seen = math.inf
    max_seen = -math.inf

    for num in range(size):
        max_seen = max(max_seen, arr[num])
        if arr[num] < max_seen:
            right = num

    for num in range(size - 1, -1, -1):
        min_seen = min(min_seen, arr[num])
        if arr[num] > min_seen:
            left = num

    return left, right


print(window(my_list))
