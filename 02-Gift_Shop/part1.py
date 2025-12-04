from pathlib import Path

with open(Path(__file__).parent / "input.txt", "r") as input:
    sum = 0
    ranges = input.read().split(",")

    for id_range in ranges:
        a, b = id_range.split("-")
        start = int(a)
        end = int(b)
        for i in range(start, end):
            str_id = str(i)
            if len(str_id) % 2 == 1:
                continue
            if str_id[: len(str_id) // 2] == str_id[len(str_id) // 2 :]:
                sum += int(str_id)

    print(sum)
