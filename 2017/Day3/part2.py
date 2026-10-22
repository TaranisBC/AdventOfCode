TARGET = 368078

def calculate_new_value(grid: dict[tuple[int, int], int], coord: tuple[int, int]) -> int:
    neighbors = []
    # Left
    neighbors.append((coord[0] - 1, coord[1]))
    # Right
    neighbors.append((coord[0] + 1, coord[1]))
    # Up
    neighbors.append((coord[0], coord[1] + 1))
    # Down
    neighbors.append((coord[0], coord[1] - 1))
    # Up-Left-Diagonal
    neighbors.append((coord[0] - 1, coord[1] + 1))
    # Down-Left-Diagonal
    neighbors.append((coord[0] - 1, coord[1] - 1))
    # Up-Right-Diagonal
    neighbors.append((coord[0] + 1, coord[1] + 1))
    # Down-Right-Diagonal
    neighbors.append((coord[0] + 1, coord[1] - 1))
    existing_values = [grid.get(coord) for coord in neighbors if grid.get(coord) is not None]
    return sum(existing_values)

coordinates = {
    (0,0) : 1
}


last_coordinate = (0,0)
direction = "R"
value = 1

while value < TARGET:
    if direction == "R":
        new_coordinate = (last_coordinate[0] + 1, last_coordinate[1])
        new_value = calculate_new_value(coordinates, new_coordinate)
        coordinates[new_coordinate] = new_value
        last_coordinate = new_coordinate
        value = new_value
        if coordinates.get((new_coordinate[0], new_coordinate[1] + 1)) is None:
            direction = "U"
            continue

    if direction == "U":
        new_coordinate = (last_coordinate[0], last_coordinate[1] + 1)
        new_value = calculate_new_value(coordinates, new_coordinate)
        coordinates[new_coordinate] = new_value
        last_coordinate = new_coordinate
        value = new_value
        if coordinates.get((new_coordinate[0] - 1, new_coordinate[1])) is None:
            direction = "L"
            continue

    if direction == "L":
        new_coordinate = (last_coordinate[0] - 1, last_coordinate[1])
        new_value = calculate_new_value(coordinates, new_coordinate)
        coordinates[new_coordinate] = new_value
        last_coordinate = new_coordinate
        value = new_value
        if coordinates.get((new_coordinate[0], new_coordinate[1] - 1)) is None:
            direction = "D"
            continue

    if direction == "D":
        new_coordinate = (last_coordinate[0], last_coordinate[1] - 1)
        new_value = calculate_new_value(coordinates, new_coordinate)
        coordinates[new_coordinate] = new_value
        last_coordinate = new_coordinate
        value = new_value
        if coordinates.get((new_coordinate[0] + 1, new_coordinate[1])) is None:
            direction = "R"
            continue


print(value)