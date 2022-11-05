# Given an integer array, find the max sum subarray of size k, where k is a positive integer.
import math


def max_subarray(my_list, size):
    max_result = -math.inf
    running_sum = 0

    for i in range(len(my_list)):
        running_sum += my_list[i]
        if i >= (k - 1):
            max_result = max(max_result, running_sum)
            running_sum -= my_list[i - (k - 1)]
    return max_result


custom_list = [1, 2, 3, 4, 5, 6, 7, 8]
k = 3
print(max_subarray(custom_list, k))
