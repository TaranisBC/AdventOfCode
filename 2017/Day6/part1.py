#banks = [0,2,7,0]
banks = [0,5,10,0,11,14,13,4,11,8,8,7,1,4,12,11]

seen_combinations = []

str_banks = [str(x) for x in banks]
seen_combinations.append("".join(str_banks))

cycles = 0
first_repeated = ""
while True:
    cycles += 1
    max_blocks = max(banks)
    starting_block = banks.index(max_blocks)
    banks[starting_block] = 0
    current = starting_block
    for i in range(max_blocks):
        current = current + 1
        if current > len(banks) - 1:
            current = 0
        banks[current] += 1

    new_combination = "".join([str(x) for x in banks])
    if new_combination in seen_combinations:
        # Added this for part 2
        first_repeated = new_combination
        break
    else:
        seen_combinations.append(new_combination)

print(cycles)
#Added this for part 2
print(cycles - seen_combinations.index(first_repeated))


