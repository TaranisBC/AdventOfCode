with open("input.txt", "r") as f:
    lines = f.read().splitlines()

initial_pos = lines[0].index("S")
lines = lines[1:]

laser_positions = set()
laser_positions.add(initial_pos)
split_count = 0
for line in lines:
    positions_to_remove = []
    positions_to_add = []
    splitters = line.count("^")
    if splitters == 0:
        continue

    splitter_indexes = []
    for i in range(len(line)):
        if line[i] == "^":
            splitter_indexes.append(i)
    for position in laser_positions:
        if position in splitter_indexes:
            split_count += 1
            positions_to_remove.append(position)
            positions_to_add.append(position - 1)
            positions_to_add.append(position + 1)
    for position in positions_to_remove:
        laser_positions.remove(position)
    for position in positions_to_add:
        laser_positions.add(position)

print(split_count)