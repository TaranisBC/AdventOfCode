with open("/home/bruno/adventofcode/2024/Day9/input.txt", "r") as puzzle:
    disk_map = puzzle.readline()

file_id = 0
spaced_map = ""
sectors = []
for i in range(len(disk_map)):
    space = int(disk_map[i])
    if i % 2 == 0:
        for j in range(space):
            sectors.append(file_id)

        file_id += 1
    else:
        for j in range(space):
            sectors.append(".")

# Since we are not adding new files, go back to the last inserted file id
file_id -= 1

while '.' in sectors:
    file_to_move = sectors.pop()
    if file_to_move == '.':
        pass
    else:
        new_sector = sectors.index('.')
        sectors[new_sector] = file_to_move


checksum = 0

for i in range(len(sectors)):
    if sectors[i] != '.':
        checksum += i * int(sectors[i])

print(checksum)