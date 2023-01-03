# this function adds 1 to every block within the range of the coordinates (x, y)
# block is within range if it can be reach within n number of steps
def block_range(grid, x, y, steps):
    # Convert coordinates from index-based 1 to index-based 0
    x -= 1
    y -= 1

    # Add 1 to the specified location
    grid[x][y] += 1

    # Add 1 to all reachable locations
    for i in range(1, steps + 1):
        # Check if the coordinates are within the bounds of the grid
        if x + i < len(grid):
            grid[x + i][y] += 1
        if x - i >= 0:
            grid[x - i][y] += 1
        if y + i < len(grid[0]):
            grid[x][y + i] += 1
        if y - i >= 0:
            grid[x][y - i] += 1


grid = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
block_range(grid, 1, 1, 1)
for row in grid:
    print(row)
