import math

def calculate_euclidian_distance(a, b):
    return math.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2 + (a[2] - b[2]) ** 2)

with open("input.txt", "r") as f:
    lines = f.read().splitlines()

coordinates = []
for line in lines:
    coordinates.append(list(map(int, line.split(","))))

all_distances = {}

for i in range(len(coordinates) - 1):
    print(i)
    for j in range(i+1, len(coordinates)):
        all_distances[(i, j)] = calculate_euclidian_distance(coordinates[i], coordinates[j])

sorted_distances = sorted(all_distances.items(), key=lambda x: x[1])

circuits = []

for i in range(len(coordinates)):
    circuits.append([i])

connexions = 0
while connexions < 1000:
    for i in range(len(sorted_distances)):
        if connexions == 0:
            index_to_remove = 0
            for circuit in circuits:
                if sorted_distances[i][0][1] in circuit:
                    index_to_remove = circuits.index(circuit)
                    break
            circuits[sorted_distances[i][0][0]].append(sorted_distances[i][0][1])
            circuits.pop(index_to_remove)
            connexions += 1
        else:
            first_circuit_index = 0
            second_circuit_index = 0
            for circuit in circuits:
                if sorted_distances[i][0][0] in circuit:
                    first_circuit_index = circuits.index(circuit)
                if sorted_distances[i][0][1] in circuit:
                    second_circuit_index = circuits.index(circuit)

            if first_circuit_index != second_circuit_index:
                for element in circuits[second_circuit_index]:
                    circuits[first_circuit_index].append(element)
                circuits.pop(second_circuit_index)
                connexions += 1
            else:
                connexions += 1
            if connexions == 1000:
                break

circuits.sort(key=len, reverse=True)
print(len(circuits[0]) * len(circuits[1]) * len(circuits[2]))