class Rectangle:
    def __init__(self, corner1, corner2):
        self.corner1 = corner1
        self.corner2 = corner2
        self.dx = abs(corner1[0] - corner2[0]) + 1
        self.dy = abs(corner1[1] - corner2[1]) + 1

    def area(self):
        return self.dx * self.dy

with open("input.txt", "r") as f:
    lines = f.read().splitlines()

coordinates = []
for line in lines:
    coordinates.append(list(map(int, line.split(","))))

areas = []
rectangles = []
for i in range(len(coordinates) - 1):
    for j in range(i + 1, len(coordinates)):
        rectangle = Rectangle(coordinates[i], coordinates[j])
        areas.append(rectangle.area())
        rectangles.append(rectangle)

print(max(areas))

sorted_coordinates = sorted(coordinates, key=lambda coord: (coord[0], coord[1]))
print(sorted_coordinates)