from pathlib import Path


def check_valid(str_id):
    if len(str_id) < 2:
        return True
    for seg_len in range(1, len(str_id) // 2 + 1):
        if len(str_id) % seg_len != 0:
            continue
        segs = [str_id[i : i + seg_len] for i in range(0, len(str_id), seg_len)]
        # If all segments are the same then invalid
        if all([seg == segs[0] for seg in segs]):
            return False
    return True


with open(Path(__file__).parent / "input.txt", "r") as input:
    sum = 0
    ranges = input.read().split(",")

    for id_range in ranges:
        a, b = id_range.split("-")
        start = int(a)
        end = int(b)
        for i in range(start, end):
            str_id = str(i)
            if check_valid(str_id):
                continue
            sum += int(str_id)

    print(sum)
