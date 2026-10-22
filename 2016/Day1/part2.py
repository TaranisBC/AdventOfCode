with open("input.txt") as f:
    data = f.read()

directions: list[str] = data.split(", ")
print(len(directions))

facing_direction: int = 1

visited: list[str] = ["0, 0"]
current_x: int = 0
current_y: int = 0
found = False

count = 0
for direction in directions:
    count += 1
    print(count)
    rotation = direction[0]
    block_amount = int(direction[1:])

    if rotation == "R":
        facing_direction += 1
        if facing_direction > 4:
            facing_direction -= 4
    else:
        facing_direction -= 1
        if facing_direction < 1:
            facing_direction += 4

    if facing_direction == 1:
        for i in range (block_amount):
            current_y += 1
            coordinate = f"{current_x}, {current_y}"
            if coordinate in visited:
                found = True
                break
            else:
                visited.append(coordinate)
    elif facing_direction == 2:
        for i in range(block_amount):
            current_x += 1
            coordinate = f"{current_x}, {current_y}"
            if coordinate in visited:
                found = True
                break
            else:
                visited.append(coordinate)
    elif facing_direction == 3:
        for i in range (block_amount):
            current_y -= 1
            coordinate = f"{current_x}, {current_y}"
            if coordinate in visited:
                found = True
                break
            else:
                visited.append(coordinate)
    elif facing_direction == 4:
        for i in range(block_amount):
            current_x -= 1
            coordinate = f"{current_x}, {current_y}"
            if coordinate in visited:
                found = True
                break
            else:
                visited.append(coordinate)

    if found:
        break


total_block_distance = abs(current_x) + abs(current_y)
print(total_block_distance)