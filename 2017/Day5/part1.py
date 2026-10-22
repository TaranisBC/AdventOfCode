with open("input.txt", "r") as f:
    instructions = f.read().splitlines()

jumps = [int(x) for x in instructions]

current_position = 0
total_jumps = 0
while True:
    initial_position = current_position
    if jumps[current_position] >= 3:
        jumps[current_position] -= 1
        current_position += jumps[current_position] + 1
    elif jumps[current_position] == 0:
        jumps[current_position] += 1
    else:
        jumps[current_position] += 1
        current_position += jumps[current_position] - 1


    total_jumps += 1
    if current_position >= len(jumps) or current_position < 0:
         break

print(total_jumps)