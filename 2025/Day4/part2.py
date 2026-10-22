def calculate_neigbor_rolls(full_grid, coordinate):
    rolls = 0
    #Right
    if full_grid[coordinate[0]][coordinate[1] + 1] == "@":
        rolls += 1
    # Left
    if full_grid[coordinate[0]][coordinate[1] - 1] == "@":
        rolls += 1
    # Up
    if full_grid[coordinate[0] - 1][coordinate[1]] == "@":
        rolls += 1
    # Down
    if full_grid[coordinate[0] + 1][coordinate[1]] == "@":
        rolls += 1
    # Right-Up
    if full_grid[coordinate[0] - 1][coordinate[1] + 1] == "@":
        rolls += 1
    # Right-Down
    if full_grid[coordinate[0] + 1][coordinate[1] + 1] == "@":
        rolls += 1
    # Left-Up
    if full_grid[coordinate[0] - 1][coordinate[1] - 1] == "@":
        rolls += 1
    # Left-Down
    if full_grid[coordinate[0] + 1][coordinate[1] - 1] == "@":
        rolls += 1

    return rolls



with open("input.txt", "r") as file:
    lines = file.read().splitlines()

grid = []
grid.append("." * (len(lines[0]) + 2))
for line in lines:
    grid.append("." + line + ".")
grid.append("." * (len(lines[0]) + 2))

rolls_to_remove = 0

while True:
    coordinates_to_remove = set()
    for i in range(1, len(grid) - 1):
        for j in range(1, len(grid[0]) - 1):
            if grid[i][j] == "@" and calculate_neigbor_rolls(grid, (i,j)) < 4:
                coordinates_to_remove.add((i,j))
                rolls_to_remove += 1
    if len(coordinates_to_remove) == 0:
        break
    for element in coordinates_to_remove:
        grid[element[0]] = grid[element[0]][:element[1]] + "x" + grid[element[0]][element[1] + 1:]

print(rolls_to_remove)
