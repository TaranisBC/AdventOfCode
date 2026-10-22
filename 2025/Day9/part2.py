from itertools import groupby

DIRS = [(0,1),(1,0),(0,-1),(-1,0)]  # right, down, left, up

class Rectangle:
    def __init__(self, corner1, corner2):
        self.corner1 = tuple(corner1)
        self.corner2 = tuple(corner2)
        self.corner3 = (corner1[0], corner2[1])
        self.corner4 = (corner2[0], corner1[1])
        self.corners = [self.corner1, self.corner2, self.corner3, self.corner4]
        self.dx = abs(corner1[0] - corner2[0]) + 1
        self.dy = abs(corner1[1] - corner2[1]) + 1

    def create_cells(self):
        cells = []
        min_y, max_y = min([self.corner1[0], self.corner2[0]]), max([self.corner1[0], self.corner2[0]])
        min_x, max_x = min([self.corner1[1], self.corner2[1]]), max([self.corner1[1], self.corner2[1]])
        for i in range(min_y, max_y+1):
            for j in range(min_x, max_x+1):
                cells.append((i, j))

        return cells



    def area(self):
        return self.dx * self.dy

## Méthode pour générer le polygone

def get_outline_ordered(outline):
    start = min(outline)
    current = start
    direction = 0
    polygon = [current]

    while True:
        for turn in [0, 1, -1, 2]:  # straight, right, left, back
            d = DIRS[(direction + turn) % 4]
            nxt = (current[0] + d[0], current[1] + d[1])
            if nxt in outline:
                current = nxt
                direction = (direction + turn) % 4
                break

        if current == start:
            break
        polygon.append(current)

    return polygon

def point_on_segment(px, py, x1, y1, x2, y2):
    # check colinearity via cross product
    dx1 = px - x1
    dy1 = py - y1
    dx2 = x2 - x1
    dy2 = y2 - y1
    if dx1 * dy2 - dy1 * dx2 != 0:
        return False
    # check bounding box
    return min(x1, x2) <= px <= max(x1, x2) and min(y1, y2) <= py <= max(y1, y2)


def point_in_polygon(px, py, edges):
    """
    polygon: list of ordered boundary points (output of get_outline_ordered)
    returns True if point is INSIDE or ON boundary
    """

    # Check boundary first
    for (x1, y1), (x2, y2) in edges:
        if point_on_segment(px, py, x1, y1, x2, y2):
            return True

    # Ray-casting
    crossings = 0
    for (x1, y1), (x2, y2) in edges:
        # Does this edge cross the horizontal ray at y = py?
        if (y1 > py) != (y2 > py):
            # Compute x-intersection
            x_int = x1 + (py - y1) * (x2 - x1) / (y2 - y1)
            if x_int < px:
                crossings += 1

    return (crossings % 2) == 1


with open("input.txt", "r") as f:
    lines = f.read().splitlines()

coordinates = []
for line in lines:
    coordinates.append(list(map(int, line.split(","))))

sorted_coordinates = sorted(coordinates, key=lambda coord: (coord[0], coord[1]))
horizontal_groups = groupby(sorted_coordinates, key=lambda coord: (coord[0]))

sorted_vertical_coordinates = sorted(coordinates, key=lambda coord: (coord[1], coord[0]))
vertical_groups = groupby(sorted_vertical_coordinates.copy(), key=lambda coord: (coord[1]))

horizontal_dict = {}

for key, group in horizontal_groups:
    horizontal_dict[key] = list(group)

final_coordinates = set()

for key, value in horizontal_dict.items():
    x1 = value[0][1]
    x2 = value[-1][1]
    for x in range(x1, x2 + 1):
        final_coordinates.add((key, x))

vertical_dict = {}

for key, group in vertical_groups:
    vertical_dict[key] = list(group)

for key, value in vertical_dict.items():
    y1 = value[0][0]
    y2 = value[-1][0]
    for y in range(y1, y2 + 1):
        final_coordinates.add((y, key))

polygone = get_outline_ordered(final_coordinates)

edges = [(polygone[i], polygone[(i+1) % len(polygone)])
         for i in range(len(polygone))]


areas = []
rectangles = []

for i in range(len(coordinates) - 1):
    print(i)
    for j in range(i + 1, len(coordinates)):
        print(j)
        rect = Rectangle(coordinates[i], coordinates[j])

        valid = True
        for cx, cy in rect.corners:
            if not point_in_polygon(cx, cy, edges):
                valid = False
                break

        if valid:
            areas.append(rect.area())
            rectangles.append(rect)

print(max(areas))
