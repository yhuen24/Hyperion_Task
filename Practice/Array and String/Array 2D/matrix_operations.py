def take_input():
    user_input = []
    print("Enter your matrix dimension")
    row, col = map(int, input().split())
    print(f"Enter your {row}x{col} matrix below: ")
    for _ in range(row):
        user_input.append(list(map(int, input().split())))

    return user_input


matrix1 = take_input()
matrix2 = take_input()

for row in matrix1:
    print(row)

for row in matrix2:
    print(row)
