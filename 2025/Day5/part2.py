with open("input.txt", "r") as f:
    lines = f.read().splitlines()

fresh_ranges = []
for line in lines:
    if "-" in line:
        limits = line.split("-")
        fresh_ranges.append([int(limits[0]), int(limits[1])])
    elif line == "":
        break


fresh_ranges.sort()

while True:
    new_ranges = []
    for i in range(len(fresh_ranges)):
        r = fresh_ranges[i]
        start, end = r
        if len(new_ranges) == 0:
            new_ranges.append(r)
        else:
            highest_range = new_ranges[-1]
            if start > highest_range[1]:
                new_ranges.append(r)
            elif start >= highest_range[0] and end > highest_range[1]:
                new_ranges[-1] = [new_ranges[-1][0], end]

    if len(fresh_ranges) == len(new_ranges):
        break
    else:
        fresh_ranges = new_ranges

fresh_id_total = 0
for r in fresh_ranges:
    total_ids = r[1] - r[0] + 1
    fresh_id_total += total_ids

print(fresh_id_total)

