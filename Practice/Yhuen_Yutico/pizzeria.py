def dfs(grid, moves, row, col, visited):
    # check if the current position is out of bounds or if we have reached the maximum number of moves
    if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]) or moves < 0:
        return

    # check if position has been visited in the past
    if (row, col) in visited:
        return
    # add (row, col) as tuple in visited set if is not visited in the past
    grid[row][col] += 1
    visited.add((row, col))
    # goes up
    dfs(grid, moves - 1, row + 1, col, visited)
    # goes down
    dfs(grid, moves - 1, row - 1, col, visited)
    # goes right
    dfs(grid, moves - 1, row, col + 1, visited)
    # goes left
    dfs(grid, moves - 1, row, col - 1, visited)


# test the function
grid = [[0] * 5 for _ in range(5)]
move_size = 3
start = (3, 3)
dfs(grid, move_size, start[0] - 1, start[1] - 1, visited=set())

for row in grid:
    print(row)
