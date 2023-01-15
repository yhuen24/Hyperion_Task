# Given an array numbers, find the maximum sum of any contiguous subarray of the array.
# For example, given the array [34, -50, 42, 14, -5, 86], the maximum sum would be 137
# because 42 + 12 + (-5) + 86 = 137
# Note to self: use Kadane Algorithm to achieve O(n) time complexity (Dynamic Programming)
import math
subarray_input = [34, -50, 42, 14, -5, 86]
result = -math.inf
cur_sum = -math.inf

for value in subarray_input:
    cur_sum = max(cur_sum + value, value)
    result = max(result, cur_sum)

print("Result: ", result)