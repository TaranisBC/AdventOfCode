def check_possible_triangle(a: int,b: int,c: int) -> bool:
    if a + b > c and a + c > b and b + c > a:
        return True
    else:
        return False

with open("input.txt") as f:
    data = f.read().splitlines()

nb_triangles = 0

column_a = []
column_b = []
column_c = []

for line in data:
    column_a.append(int(line[2:5].strip()))
    column_b.append(int(line[7:10].strip()))
    column_c.append(int(line[12:15].strip()))

for i in range(0, len(column_a), 3):
    if check_possible_triangle(column_a[i], column_a[i+1], column_a[i+2]):
        nb_triangles += 1
    if check_possible_triangle(column_b[i], column_b[i+1], column_b[i+2]):
        nb_triangles += 1
    if check_possible_triangle(column_c[i], column_c[i+1], column_c[i+2]):
        nb_triangles += 1

print(nb_triangles)