def dfs(grid, moves, row, col, visited):
    # check if the current position is out of bounds
    if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]):
        return

    # check if the current position has already been visited
    if (row, col) in visited:
        return

    # mark the current position as visited
    visited.add((row, col))

    # add 1 to the current position in the grid
    grid[row][col] += 1

    if moves > 0:
        # continue the search in all 4 directions (up, down, left, right)
        dfs(grid, moves - 1, row + 1, col, visited)
        dfs(grid, moves - 1, row - 1, col, visited)
        dfs(grid, moves - 1, row, col + 1, visited)
        dfs(grid, moves - 1, row, col - 1, visited)


# test the function
grid = [[0] * 5 for _ in range(5)]
move_size = 3
start = (3, 3)
dfs(grid, move_size, start[0] - 1, start[1] - 1, visited=set())

for row in grid:
    print(row)