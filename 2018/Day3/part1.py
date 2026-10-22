with open("input.txt", "r") as file:
    lines = file.read().splitlines()

left_distances = []
top_distances = []
widths = []
heights = []

coordinates = []

for line in lines:
    data = line.split(" ")
    data[2] = data[2][0:len(data[2]) - 1]

    distances = data[2].split(",")
    left_distance = int(distances[0])
    top_distance = int(distances[1])

    dimensions = data[3].split("x")
    width = int(dimensions[0])
    height = int(dimensions[1])

    line_coordinates = []

    for i in range(width):
        for j in range(height):
            line_coordinates.append((i + left_distance, j + top_distance))

    coordinates.append(line_coordinates)


duplicates = set()

for i in range(len(coordinates) - 1):
    print(i)
    for j in range(i+1, len(coordinates)):
        for coordinate in coordinates[j]:
            if coordinate in coordinates[i]:
                duplicates.add(coordinate)

print(duplicates)


