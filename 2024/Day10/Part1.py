def find_starting_positions(map: list[str]) -> list[tuple[int, int]]:

    starting_positions = []
    for i in range(len(map)):
        for j in range(len(map[i])):
            if map[i][j] == '0':
                starting_positions.append((j, i))

    return starting_positions

def evaluate_position(x: int, y: int, map: list[str], tops: set) -> None:
        
    height = map[y][x]    

    if height == "9":
        tops.add((x,y))
        return
    
    # Up
    if y > 0 and int(map[y-1][x]) == int(height) + 1:
        evaluate_position(x, y-1, map, tops)

    # Down
    if y < len(map) - 1 and int(map[y+1][x]) == int(height) + 1:
        evaluate_position(x, y+1, map, tops)

    # Left
    if x > 0 and int(map[y][x-1]) == int(height) + 1:
        evaluate_position(x -1, y, map, tops)

    # Right
    if x < len(map[0]) - 1 and int(map[y][x+1]) == int(height) + 1:
        evaluate_position(x+1, y, map, tops)


if __name__ == '__main__':

    with open("input.txt", "r") as puzzle:
        puzzle_input = puzzle.read().splitlines()

    starting_positions = find_starting_positions(puzzle_input)

    
    score = 0
    for pos in starting_positions:
        summit_coordinates = set()
        evaluate_position(pos[0], pos[1], puzzle_input, summit_coordinates)
        score += len(summit_coordinates)

    print(score)

    