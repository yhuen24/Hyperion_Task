# Given an array of integers, return a new array such that each element at index i of the new array is the product of
# all the numbers in the original array except the one at i

array_list = [1, 2, 3, 4, 5]
product_list = []  # will get populated after calculation
all_product = 1
for i in array_list:  # get all product by multiplying all elements in list
    all_product *= i
for i in array_list:
    result = all_product / i
    product_list.append(int(result))
print(product_list)
