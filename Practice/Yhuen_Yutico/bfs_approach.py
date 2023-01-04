from collections import deque

# Solution
def add_one(grid, start, n):
    que = deque([start])

    # Mark the starting point as visited
    visited = set([start])

    # Initialize the number of steps taken to 0
    steps = 0

    # Loop until the queue is empty
    while que:
        # Get the size of the queue
        size = len(que)

        # Loop over all the points in the current level
        for _ in range(size):
            # Pop the first point from the queue
            point = que.popleft()

            # Get the row and column of the point
            row, col = point

            # Add one to the grid at this point
            grid[row - 1][col - 1] += 1

            # Check all the possible next steps from this point
            for r, c in ((row + 1, col), (row - 1, col), (row, col + 1), (row, col - 1)):
                # If the new point is within the grid and has not been visited
                if (1 <= r <= len(grid)) and (1 <= c <= len(grid[0])) and ((r, c) not in visited):
                    # Add the new point to the queue and mark it as visited
                    que.append((r, c))
                    visited.add((r, c))
        steps += 1
        if steps > n:
            break


# Driver Code
dimension, pizzeria_num = map(int, input().split())
grid = [[0] * dimension for _ in range(dimension)]
for _ in range(pizzeria_num):
    row, col, moves = map(int, input().split())
    start = (row, col)
    add_one(grid, start, moves)

# finding position with the highest value in the grid
result = 0
for grid_row in grid:
    result = max(result, max(grid_row))

print(result)

