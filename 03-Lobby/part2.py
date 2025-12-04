from pathlib import Path
from typing import List


def largest_joltage(bank: List[int]):
    available = bank[: len(bank) - 12]
    joltage = 0
    for i in bank[len(bank) - 12 :]:
        available.append(i)
        best = max(available)
        available = available[available.index(best) + 1 :]
        joltage = joltage * 10 + best
    return joltage


with open(Path(__file__).parent / "input.txt", "r") as input:
    total = 0
    for bank in input:
        bank = [int(i) for i in bank.strip()]
        total += largest_joltage(bank)
    print(total, "Jolts")
