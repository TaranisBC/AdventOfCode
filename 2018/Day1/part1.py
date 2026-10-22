with open("input.txt", "r") as f:
    data = f.read().splitlines()

frequency = 0

for instruction in data:
    if instruction[0] == "+":
        frequency += int(instruction[1:])
    else:
        frequency -= int(instruction[1:])

print(frequency)