with open("input.txt", "r") as f:
    battery_banks = f.read().splitlines()

total_joltage = 0

for bank in battery_banks:
    bank_provided_jolt = 0
    banks_joltage = set([int(x) for x in bank])

    highest_joltage = max(banks_joltage)
    if bank.count(str(highest_joltage)) > 1:
        bank_provided_jolt = highest_joltage * 11
        total_joltage += bank_provided_jolt
        continue

    highest_index = bank.index(str(highest_joltage))
    if highest_index == len(bank) - 1:
        banks_joltage.remove(highest_joltage)
        second_highest_joltage = max(banks_joltage)
        bank_provided_jolt = second_highest_joltage * 10 + highest_joltage
        total_joltage += bank_provided_jolt
        continue
    else:
        segments = bank.split(str(highest_joltage))
        first_segment = set([int(x) for x in segments[0]])
        second_segment = set([int(x) for x in segments[1]])

        if len(first_segment) == 0:
            bank_provided_jolt = highest_joltage * 10 + max(second_segment)
            total_joltage += bank_provided_jolt
            continue

        potential1 = bank_provided_jolt = max(first_segment) * 10 + highest_joltage
        potential2 = bank_provided_jolt = highest_joltage * 10 + max(second_segment)

        if potential1 > potential2:
            bank_provided_jolt = potential1
            total_joltage += bank_provided_jolt
        else:
            bank_provided_jolt = potential2
            total_joltage += bank_provided_jolt


print(total_joltage)

