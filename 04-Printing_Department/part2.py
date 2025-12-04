from collections import deque
from pathlib import Path

with open(Path(__file__).parent / "input.txt", "r") as input:
    grid = [row.strip() for row in input]

    total_rows = len(grid)
    total_cols = len(grid[0])

    neighbor_count = [[0] * total_cols for _ in range(total_rows)]
    queue = deque()

    # Initialize neighbor_count
    for i in range(total_rows):
        for j in range(total_cols):
            if grid[i][j] == ".":
                continue

            # Look at surrounding cells
            for di in range(-1, 2):
                if i + di < 0 or i + di >= total_rows:
                    continue
                for dj in range(-1, 2):
                    if j + dj < 0 or j + dj >= total_cols:
                        continue
                    if di == 0 and dj == 0:
                        continue

                    if grid[i + di][j + dj] != ".":
                        neighbor_count[i][j] += 1

            if neighbor_count[i][j] < 4:
                queue.append((i, j))

    # Remove rolls one by one
    ans = 0
    while queue:
        ans += 1
        i, j = queue.pop()

        # Look at surrounding cells
        for di in range(-1, 2):
            if i + di < 0 or i + di >= total_rows:
                continue
            for dj in range(-1, 2):
                if j + dj < 0 or j + dj >= total_cols:
                    continue
                if di == 0 and dj == 0:
                    continue

                neighbor_count[i + di][j + dj] -= 1
                if neighbor_count[i + di][j + dj] == 3:
                    queue.append((i + di, j + dj))

    print(ans)
