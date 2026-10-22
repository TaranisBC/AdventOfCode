with open("/home/bruno/DataDrive/adventofcode/2024/Day6/input.txt", "r") as puzzle:
    values = puzzle.read().splitlines()

guard_position = ()
direction = "up"
positions_visitees = set()

for i in range(len(values)):
    if "^" in values[i]:
        guard_position = (i, values[i].index("^"))
        break

positions_visitees.add(guard_position)

while True:
    if direction =="up":
        new_position = (guard_position[0] - 1 , guard_position[1])
        if new_position[0] < 0:
            break
        elif values[new_position[0]][new_position[1]] == "#":
            direction = "right"
        else:
            guard_position = new_position
            positions_visitees.add(new_position)
    elif direction =="down":
        new_position = (guard_position[0] + 1 , guard_position[1])
        if new_position[0] > len(values):
            break
        elif values[new_position[0]][new_position[1]] == "#":
            direction = "left"
        else:
            guard_position = new_position
            positions_visitees.add(new_position)  
    elif direction =="right":
        new_position = (guard_position[0] , guard_position[1] + 1)
        if new_position[1] > len(values[0]):
            break
        elif values[new_position[0]][new_position[1]] == "#":
            direction = "down"
        else:
            guard_position = new_position
            positions_visitees.add(new_position)
    elif direction =="left":
        new_position = (guard_position[0], guard_position[1] - 1)
        if new_position[1] < 0:
            break
        elif values[new_position[0]][new_position[1]] == "#":
            direction = "up"
        else:
            guard_position = new_position
            positions_visitees.add(new_position)

print(len(positions_visitees))