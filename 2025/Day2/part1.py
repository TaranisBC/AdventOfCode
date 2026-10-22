with open("input.txt", "r") as f:
    data = f.read()

ranges = data.split(",")

invalid_ids = []

for r in ranges:
    start, end = r.split("-")
    if len(start) % 2 == 1 and len(end) % 2 == 1 and len(start) == len(end):
        continue

    numbers = [str(i) for i in range(int(start), int(end) + 1)]
    for n in numbers:
        if len(n) % 2 == 0 and len(n) > 1:
            splices = n[:len(n)//2], n[len(n)//2:]
            if splices[0] == splices[1]:
                invalid_ids.append(int(n))

print(sum(invalid_ids))


