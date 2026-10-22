initial_row = ".^^^^^.^^^..^^^^^...^.^..^^^.^^....^.^...^^^...^^^^..^...^...^^.^.^.......^..^^...^.^.^^..^^^^^...^."
grid = [initial_row]

tarp_patterns = ["^^.", ".^^", "^..", "..^"]

for i in range(1, 400000):
    print(i)
    new_row = ""
    for j in range(len(initial_row)):
        pattern_to_match = ""
        if j-1 < 0:
            pattern_to_match += "." + grid[i-1][j] + grid[i-1][j+1]
        elif j+1 >= len(initial_row):
            pattern_to_match += grid[i - 1][j-1] + grid[i - 1][j] + "."
        else:
            pattern_to_match += grid[i - 1][j-1] + grid[i - 1][j] + grid[i - 1][j + 1]

        if pattern_to_match in tarp_patterns:
            new_row += "^"
        else:
            new_row += "."
    grid.append(new_row)

safe_tiles = 0
for lin in grid:
    safe_tiles += lin.count(".")

print(safe_tiles)

