def check_possible_triangle(a: int,b: int,c: int) -> bool:
    if a + b > c and a + c > b and b + c > a:
        return True
    else:
        return False

with open("input.txt") as f:
    data = f.read().splitlines()

nb_triangles = 0

for line in data:
    side_a = line[2:5].strip()
    side_b = line[7:10].strip()
    side_c = line[12:15].strip()
    if check_possible_triangle(int(side_a), int(side_b), int(side_c)):
        nb_triangles += 1

print(nb_triangles)