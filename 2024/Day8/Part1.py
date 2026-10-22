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
    
    node_positions = set()

    for key, value in transmitters.items():                
        unique_pairs = list(itertools.combinations(value, 2))
        for pair in unique_pairs:            
            delta_x = abs(pair[0][1] - pair[1][1])
            delta_y = abs(pair[0][0] - pair[1][0])
            node1_x = 0
            node1_y = 0
            node2_x = 0
            node2_y = 0
            if pair[0][1] < pair[1][1]:
                node1_x = pair[0][1] - delta_x
                node2_x = pair[1][1] + delta_x
            else:
                node1_x = pair[0][1] + delta_x
                node2_x = pair[1][1] - delta_x

            if pair[0][0] < pair[1][0]:
                node1_y = pair[0][0] - delta_y
                node2_y = pair[1][0] + delta_y
            else:
                node1_y = pair[0][0] + delta_y
                node2_y = pair[1][0] - delta_y

            if (0 <= node1_x < len(values[0])) and (0 <= node1_y < len(values)):
                node_positions.add((node1_y, node1_x))
            
            if (0 <= node2_x < len(values[0])) and (0 <= node2_y < len(values)):
                node_positions.add((node2_y, node2_x))

    print(len(node_positions))
            