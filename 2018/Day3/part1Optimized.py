with open("input.txt", "r") as file:
    lines = file.read().splitlines()

left_distances = []
top_distances = []
widths = []
heights = []

coordinates = {}

for line in lines:
    data = line.split(" ")
    data[2] = data[2][0:len(data[2]) - 1]

    distances = data[2].split(",")
    left_distance = int(distances[0])
    top_distance = int(distances[1])

    dimensions = data[3].split("x")
    width = int(dimensions[0])
    height = int(dimensions[1])

    for x in range(left_distance, left_distance + width):
        for y in range(top_distance, top_distance + height):
            if (x,y) in coordinates.keys():
                coordinates[(x, y)] += 1
            else:
                coordinates[(x, y)] = 1


duplucates = 0
for value in coordinates.values():
    if value > 1:
        duplucates += 1

print(duplucates)

for key, value in coordinates.items():
    print(key, value)


