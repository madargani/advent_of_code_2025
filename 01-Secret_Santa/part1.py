from pathlib import Path

with open(Path(__file__).parent / "input.txt", "r") as input:
    count = 0
    pos = 50
    for line in input:
        if line[0] == "R":
            pos = (pos + int(line[1:])) % 100
        elif line[0] == "L":
            pos = (pos - int(line[1:])) % 100

        if pos == 0:
            count += 1
    print("Password is", count)
