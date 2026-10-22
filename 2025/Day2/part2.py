with open("input.txt", "r") as f:
    data = f.read()

ranges = data.split(",")

invalid_ids = []

for r in ranges:
    start, end = r.split("-")

    numbers = [str(i) for i in range(int(start), int(end) + 1)]
    for n in numbers:
        if len(n) > 1:
            if n in (n + n)[1:-1]:
                invalid_ids.append(int(n))

print(sum(invalid_ids))
print(invalid_ids)


