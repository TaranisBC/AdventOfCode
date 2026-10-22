import itertools

if __name__ == '__main__':

    with open("input.txt", "r") as puzzle:
        values = puzzle.read().splitlines()


    transmitters = {}

    for i in range(len(values)):
        for j in range(0, len(values[0])):
            if values[i][j] != ".":
                if values[i][j] in transmitters:
                    transmitters[values[i][j]].append((i,j))
                else:
                    transmitters[values[i][j]] = [(i,j)]

    for key, value in transmitters.items():
        print(f"{key} : {value}")
    
    node_positions = set()

    for key, value in transmitters.items():                
        unique_pairs = list(itertools.combinations(value, 2))
        for pair in unique_pairs:            
            delta_x = abs(pair[0][1] - pair[1][1])
            delta_y = abs(pair[0][0] - pair[1][0])

            node_positions.add(pair[0])
            
            direction = ""

            if pair[0][1] < pair[1][1]:
                direction = "ltr"
            else:
                direction = "rtl"    

            if direction == "ltr":
                x = pair[0][1]
                y = pair[0][0]
                while True:
                    x = x - delta_x
                    y = y - delta_y
                    if x >=0 and y >= 0:
                        node_positions.add((y, x))
                    else:
                        break
                
                x = pair[0][1]
                y = pair[0][0]

                while True:
                    x = x + delta_x
                    y = y + delta_y
                    if x < len(values[0]) and y < len(values):
                        node_positions.add((y, x))
                    else:
                        break

            else:
                x = pair[0][1]
                y = pair[0][0]
                while True:
                    x = x + delta_x
                    y = y - delta_y
                    if x < len(values[0]) and y >= 0:
                        node_positions.add((y, x))
                    else:
                        break
                
                x = pair[0][1]
                y = pair[0][0]

                while True:
                    x = x - delta_x
                    y = y + delta_y
                    if x >= 0 and y < len(values):
                        node_positions.add((y, x))
                    else:
                        break
                

    print(len(node_positions))
            