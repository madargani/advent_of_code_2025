from pathlib import Path

with open(Path(__file__).parent / "input.txt", "r") as input:
    total = 0
    for bank in input:
        bank = [i for i in bank.strip()]
        battery_a = max(bank[:-1])
        bank = bank[bank.index(battery_a) + 1 :]
        battery_b = max(bank)
        total += int(battery_a + battery_b)
    print(total, "Jolts")
