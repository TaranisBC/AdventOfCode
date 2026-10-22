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


grid = [["." for _ in range(7)] for _ in range(3)]

grid = rect(grid, 3, 2)
grid = rotate_column(grid, 1, 1)
grid = rotate_row(grid, 0, 4)
grid = rotate_column(grid, 1, 1)

for line in grid:
    print(line)