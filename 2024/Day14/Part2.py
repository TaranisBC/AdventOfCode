import os

if __name__ == '__main__':

    with open("/home/bruno/adventofcode/2024/Day14/input.txt", "r") as puzzle:
        puzzle_lines = puzzle.read().splitlines()

    starting_positions = []
    velocities = []

    for line in puzzle_lines:
        data = line.split(" ")
        starting_positions.append(data[0][2:])
        velocities.append(data[1][2:])

    grid_line = ["."] * 101


    positions = [tuple(map(int, item.split(','))) for item in starting_positions]
    speeds = [tuple(map(int, item.split(','))) for item in velocities]

    seconds = 0
    while True:
        seconds += 1
        for i in range(len(positions)):    

            final_x = (positions[i][0] + speeds[i][0]) % 101

            final_y = (positions[i][1] + speeds[i][1]) % 103

            positions[i] = (final_x, final_y)        

        
        final_grid = []
        for i in range(103):
            final_grid.append(grid_line.copy())   


        for position in positions:        
            final_grid[position[1]][position[0]] = "#"
            
        for line in final_grid:
            if "#####" in ("").join(line):
                print(seconds)
                for ln in final_grid:
                    print(("").join(ln))
                input("")
                break
        
        os.system('clear')
    



