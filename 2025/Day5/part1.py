with open("input.txt", "r") as f:
    lines = f.read().splitlines()

fresh_ranges = []
ingredients = []
for line in lines:
    if line != "":
        if "-" in line:
            limits = line.split("-")
            fresh_ranges.append((int(limits[0]), int(limits[1])))
        else:
            ingredients.append(int(line))


fresh = 0
for ingredient in ingredients:
    for ranges in fresh_ranges:
        if ranges[0] <= ingredient <= ranges[1]:
            fresh += 1
            break

print(fresh)

