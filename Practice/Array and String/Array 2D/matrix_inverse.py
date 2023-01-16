import math
import numpy as np


def take_input():
    user_input = []
    print("Enter your matrix dimension")
    row, col = map(int, input().split())
    print(f"Enter your {row}x{col} matrix below: ")
    for _ in range(row):
        user_input.append(list(map(int, input().split())))

    return user_input


# returns the adjugate version of the passed matrix
def solve_adjugate(matrix):
    matrix_adj = [[matrix[1][1], -matrix[0][1]], [-matrix[1][0], matrix[0][0]]]
    return matrix_adj


# accepts 2x2 matrix
# returns a determinant of a passed matrix (integer)
def solve_determinant(matrix):
    # for 2x2 matrix
    if len(matrix) == 2 and len(matrix[0]) == 2:
        # det(matrix) = (ad) - (bc)    -> [[a, b], [c, d]]
        det = (matrix[0][0] * matrix[1][1]) - (matrix[0][1] * matrix[1][0])
    # for 3x3 matrix (diagonal method)
    else:
        a = matrix[0][0]
        b = matrix[0][1]
        c = matrix[0][2]
        d = matrix[1][0]
        e = matrix[1][1]
        f = matrix[1][2]
        g = matrix[2][0]
        h = matrix[2][1]
        i = matrix[2][2]
        # [a, b, c]
        # [d, e, f]
        # [g, h, i]
        # from up going down  -> from down going up
        det = (a * e * i) + (b * f * g) + (c * d * h) - (c * e * g) - (b * d * i) - (a * f * h)
        # Bottom - Top method
        # det = ((a * e * i) + (b * f * g) + (c * d * h)) - ((c * e * g) + (b * d * i) + (a * f * h))
    return det


# returns the inverse version of the passed matrix
def solve_inverse(adj_matrix, determinant):
    result = []
    if len(adj_matrix) == 2 and len(adj_matrix[0]) == 2:
        for row in adj_matrix:
            row_list = []
            for col in row:
                row_list.append(round(col / determinant, 2))
            result.append(row_list)
    else:
        for row in adj_matrix:
            row_list = []
            for col in row:
                row_list.append(col * round(1 / determinant, 2))
            result.append(row_list)
    return result


# returns the transposed version of the passed matrix
def solve_transpose(matrix):
    new_col = len(matrix)
    new_row = len(matrix[0])
    matrix_transposed = [[0 for _ in range(new_col)] for _ in range(new_row)]
    for i in range(new_row):
        for j in range(new_col):
            matrix_transposed[j][i] = matrix[i][j]
    return matrix_transposed


# returns the minor of given position (Integer)
def solve_minor(matrix, row_pos, col_pos):
    new_matrix = []
    for i in range(len(matrix)):
        if i != row_pos:
            row_matrix = []
            for j in range(len(matrix[i])):
                if j != col_pos:
                    row_matrix.append(matrix[i][j])
            new_matrix.append(row_matrix)
    result = solve_determinant(new_matrix)
    return result


def solve_cofactor(minor, row_pos, col_pos):
    cofactor = int(math.pow(-1, (row_pos + col_pos))) * minor
    return cofactor


matrix = take_input()
matrix_determinant = solve_determinant(matrix)
print(f"The determinant of your matrix is: {matrix_determinant}")
# matrix_adjugate = solve_adjugate(matrix)
# matrix_transpose = solve_transpose(matrix)
# matrix_cofactor = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
# for i in range(len(matrix)):
#     for j in range(len(matrix[0])):
#         matrix_minor = solve_minor(matrix, i, j)
#         matrix_cofactor[i][j] = solve_cofactor(matrix_minor, i, j)
# matrix_adjoint = solve_transpose(matrix_cofactor)
# print("The Adjoint of your matrix are:")
# for row in matrix_adjoint:
#     print(row)
# matrix_inverse = solve_inverse(matrix_adjoint, matrix_determinant)

# print("The cofactor of your matrix are:")
# for row in matrix_cofactor:
#     print(row)
# print("The inverse of your matrix are:")
# for row in matrix_inverse:
#     print(row)
