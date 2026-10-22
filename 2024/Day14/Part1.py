if __name__ == '__main__':

    with open("input.txt", "r") as puzzle:
        puzzle_lines = puzzle.read().splitlines()

    starting_positions = []
    velocities = []

    for line in puzzle_lines:
        data = line.split(" ")
        starting_positions.append(data[0][2:])
        velocities.append(data[1][2:])

    final_positions = []

    for i in range(len(starting_positions)):
        initial_coordinates = starting_positions[i].split(",")
        speeds = velocities[i].split(",")

        final_x = (int(initial_coordinates[0]) + (100 * int(speeds[0]))) % 101
        final_y = (int(initial_coordinates[1]) + (100 * int(speeds[1]))) % 103

        final_positions.append((final_x, final_y))

    quadrant_1 = []
    quadrant_2 = []
    quadrant_3 = []
    quadrant_4 = []

    for pos in final_positions:
        if pos[0] < 101 // 2 and pos[1] < 103//2 :
            quadrant_2.append(pos)
        elif pos[0] > 101 // 2 and pos[1] < 103//2 :
            quadrant_1.append(pos)
        elif pos[0] < 101 // 2 and pos[1] > 103//2 :
            quadrant_3.append(pos)
        elif pos[0] > 101 // 2 and pos[1] > 103//2 :
            quadrant_4.append(pos)

    safety_factor = len(quadrant_1) * len(quadrant_2) * len(quadrant_3) * len(quadrant_4)
    print(safety_factor)