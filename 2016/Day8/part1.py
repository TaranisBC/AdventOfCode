def rect(current_grid: list[list[str]], width: int, height: int) -> list[list[str]]:
    for i in range (height):
        for j in range (width):
            current_grid[i][j] = '#'
    return current_grid

def rotate_row(current_grid: list[list[str]], row: int, shift: int) -> list[list[str]]:
    new_line = []
    new_line.extend(["." for _ in range(len(current_grid[0]))])

    current_row = current_grid[row]
    for i in range(len(new_line)):
        new_pos = i + shift
        if new_pos >= len(new_line):
            new_pos -= len(new_line)

        new_line[new_pos] = current_row[i]

    current_grid[row] = new_line
    return current_grid


def rotate_column(current_grid: list[list[str]], column: int, shift: int) -> list[list[str]]:
    new_col = []
    new_col.extend(["." for _ in range(len(current_grid))])

    current_col = []
    for i in range(len(current_grid)):
        current_col.append(current_grid[i][column])

    for i in range(len(new_col)):
        new_pos = i + shift
        if new_pos >= len(new_col):
            new_pos -= len(new_col)

        new_col[new_pos] = current_col[i]

    for i in range(len(current_grid)):
        current_grid[i][column] = new_col[i]

    return current_grid


with open("input.txt") as f:
    data = f.read().splitlines()

grid = [["." for _ in range(50)] for _ in range(6)]

for line in data:
    if "rect" in line:
        directions = line.split(" ")
        sizes = directions[1].split("x")

        grid = rect(grid, int(sizes[0]), int(sizes[1]))

    elif "column" in line:
        directions = line.split(" ")
        column = int(directions[2].split("=")[1])
        shift = int(directions[4])

        grid = rotate_column(grid, column, shift)

    else:
        directions = line.split(" ")
        row = int(directions[2].split("=")[1])
        shift = int(directions[4])

        grid = rotate_row(grid, row, shift)


pixels = 0
for line in grid:
    pixels += line.count("#")

print(pixels)

for line in grid:
    for i in range(len(line)):
        if line[i] == ".":
            line[i] = " "

    print(''.join(line))
