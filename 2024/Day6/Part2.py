with open("/home/bruno/DataDrive/adventofcode/2024/Day6/input.txt", "r") as puzzle:
    map = puzzle.read().splitlines()

guard_position = ()

for i in range(len(map)):
    if "^" in map[i]:
        initial_guard_position = (i, map[i].index("^"), "up")
        break

possibilites = 0

for i in range(0, len(map)):
    for j in range(0, len(map[0])):
        positions_visitees = set()
        positions_visitees.add(initial_guard_position)
        guard_position = initial_guard_position
        values = map.copy()
        direction = "up"


        if values[i][j] != "#":
            line_checked = values[i]
            new_line = line_checked[0:j] + "#" + line_checked[j+1:]
            values[i] = new_line

            while True:
                if direction =="up":
                    new_position = (guard_position[0] - 1 , guard_position[1], direction)
                    if new_position[0] < 0:
                        break
                    elif values[new_position[0]][new_position[1]] == "#":
                        direction = "right"
                    else:
                        guard_position = new_position
                        if new_position in positions_visitees:
                            possibilites += 1
                            break
                        positions_visitees.add(new_position)
                    
                elif direction =="down":
                    new_position = (guard_position[0] + 1 , guard_position[1], direction)
                    if new_position[0] > len(values) - 1:
                        break
                    elif values[new_position[0]][new_position[1]] == "#":
                        direction = "left"
                    else:
                        guard_position = new_position
                        if new_position in positions_visitees:
                            possibilites += 1
                            break
                        positions_visitees.add(new_position)
                elif direction =="right":
                    new_position = (guard_position[0] , guard_position[1] + 1, direction)
                    if new_position[1] > len(values[0]) - 1:
                        break
                    elif values[new_position[0]][new_position[1]] == "#":
                        direction = "down"
                    else:
                        guard_position = new_position
                        if new_position in positions_visitees:
                            possibilites += 1
                            break
                        positions_visitees.add(new_position)
                elif direction =="left":
                    new_position = (guard_position[0], guard_position[1] - 1, direction)
                    if new_position[1] < 0:
                        break
                    elif values[new_position[0]][new_position[1]] == "#":
                        direction = "up"
                    else:
                        guard_position = new_position
                        if new_position in positions_visitees:
                            possibilites += 1
                            break
                        positions_visitees.add(new_position)            

print(possibilites)