from collections import deque

# Solution
def add_one(grid, start, n):
    que = deque([start])
    visited = set([start])
    steps = 0

    while que:
        size = len(que)

        # Loop over all the position in the current level
        for _ in range(size):
            # Pop the first position from the queue
            position = que.popleft()

            # Using Unpacking, get row and col of the position
            row, col = position
            grid[row - 1][col - 1] += 1

            # Listing all the possible steps (Up -> Down -> Left -> Right)
            possible_step = ((row + 1, col), (row - 1, col), (row, col - 1), (row, col + 1))
            # Check all the possible next steps
            for r, c in possible_step: #
                # Check if r and c are within valid position meaning not out of bounds
                valid_position = (1 <= r <= len(grid)) and (1 <= c <= len(grid[0]))
                if valid_position and (r, c) not in visited:
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

