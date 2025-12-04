from pathlib import Path

with open(Path(__file__).parent / "input.txt", "r") as input:
    grid = [row.strip() for row in input]

    ans = 0

    total_rows = len(grid)
    total_cols = len(grid[0])
    for i in range(total_rows):
        for j in range(total_cols):
            if grid[i][j] == ".":
                continue

            # Look at surrounding cells
            roll_count = 0
            for di in range(-1, 2):
                if i + di < 0 or i + di >= total_rows:
                    continue
                for dj in range(-1, 2):
                    if j + dj < 0 or j + dj >= total_cols:
                        continue
                    if di == 0 and dj == 0:
                        continue

                    if grid[i + di][j + dj] != ".":
                        roll_count += 1

            if roll_count < 4:
                ans += 1

    print(ans)
