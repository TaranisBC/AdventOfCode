with open("input.txt", "r") as f:
    battery_banks = f.read().splitlines()

total_joltage = 0

for bank in battery_banks:
    bank_provided_jolt = ""

    calculate_joltage = True
    while len(bank_provided_jolt) < 12:
        if calculate_joltage:
            banks_joltage = set([int(x) for x in bank])

        highest_number = max(banks_joltage)

        highest_number_index = bank.find(str(highest_number))

        if highest_number_index < len(bank) - (12 - len(bank_provided_jolt) - 1):
            bank = bank[highest_number_index + 1:]
            bank_provided_jolt += str(highest_number)
            calculate_joltage = True
        else:
            banks_joltage.remove(highest_number)
            calculate_joltage = False


    print(bank_provided_jolt)
    total_joltage += int(bank_provided_jolt)

print(total_joltage)

