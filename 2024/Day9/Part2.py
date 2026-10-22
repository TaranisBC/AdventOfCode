with open("input.txt", "r") as puzzle:
    disk_map = puzzle.readline()

file_id = 0
spaced_map = ""
sectors = []
file_dict = {}
for i in range(len(disk_map)):
    space = int(disk_map[i])
    if i % 2 == 0:
        for j in range(space):
            sectors.append(file_id)
            if file_id in file_dict:
                file_dict[file_id] += 1
            else:
                file_dict[file_id] = 1

        file_id += 1
    else:
        for j in range(space):
            sectors.append(".")

file_id -= 1

while file_id > 0:
    print(file_id)
    free_space_needed = file_dict[file_id]
    last_sector_block = sectors.index(file_id)
    free_space = 0
    for i in range(0, last_sector_block):
        if sectors[i] == ".":
            free_space += 1
        else:
            free_space = 0
        
        if free_space == free_space_needed:
            pos = i
            while file_id in sectors:
                sectors[sectors.index(file_id)] = "."
            while free_space_needed > 0:
                sectors[pos] = file_id
                pos -= 1
                free_space_needed -= 1
            break
    file_id -= 1

checksum = 0
for i in range(len(sectors)):
    if sectors[i] != ".":
        checksum += sectors[i] * i

print(checksum)