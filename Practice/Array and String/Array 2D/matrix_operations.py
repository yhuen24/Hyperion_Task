def take_input():
    user_input = []
    print("Enter your matrix dimension")
    row, col = map(int, input().split())
    print(f"Enter your {row}x{col} matrix below: ")
    for _ in range(row):
        user_input.append(list(map(int, input().split())))

    return user_input


def matrix_multiply(matrix1, matrix2):
    if len(matrix1[0]) != len(matrix2):
        return None
    new_row = len(matrix1)
    new_col = len(matrix2[0])
    result = [[0 for _ in range(new_col)] for _ in range(new_row)]

    for i in range(len(matrix1)):
        for j in range(len(matrix2[i])):
            for k in range(len(matrix1[0])):
                result[i][j] += matrix1[i][k] * matrix2[k][j]
    return result


def scalar_multiply(num, matrix):
    new_row = len(matrix)
    new_col = len(matrix[0])
    result = [[0 for _ in range(new_col)] for _ in range(new_row)]
    for i in range(new_row):
        for j in range(new_col):
            result[i][j] = matrix[i][j] * num
    return result


matrix1 = take_input()
num = int(input("Enter Scalar value: "))
result = scalar_multiply(num, matrix1)
for row in result:
    print(row)
