with open("input.txt") as f:
    data = f.read()

directions: list[str] = data.split(", ")
print(directions)

facing_direction: int = 1

delta_x = 0
delta_y = 0

for direction in directions:
    rotation = direction[0]
    block_amount = direction[1:]

    if rotation == "R":
        facing_direction += 1
        if facing_direction > 4:
            facing_direction -= 4
    else:
        facing_direction -= 1
        if facing_direction < 1:
            facing_direction += 4

    if facing_direction == 1:
        delta_y += int(block_amount)
    elif facing_direction == 2:
        delta_x += int(block_amount)
    elif facing_direction == 3:
        delta_y -= int(block_amount)
    elif facing_direction == 4:
        delta_x -= int(block_amount)

total_block_distance = abs(delta_x) + abs(delta_y)
print(total_block_distance)