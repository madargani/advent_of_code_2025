from pathlib import Path

with open(Path(__file__).parent / "input.txt", "r") as input:
    count = 0
    pos = 50
    for line in input:
        dist = int(line[1:])
        count += dist // 100
        dist %= 100

        if line[0] == "R":
            if pos == 100:
                pos = 0
            pos += dist
            if pos >= 100:
                count += 1
            pos %= 100

        elif line[0] == "L":
            if pos == 0:
                pos = 100
            pos -= dist
            if pos <= 0:
                count += 1
            pos %= 100

        print(line.strip(), pos, count)

    print("Password is", count)
