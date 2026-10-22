with open("input.txt", "r") as f:
    lines = f.read().splitlines()

initial_pos = lines[0].index("S")
lines = lines[1:]
laser_count = [0] * len(lines[0])
laser_count[initial_pos] = 1
print(laser_count)
timeline_count = 0

for line in lines:
    for i in range(len(line)):
        if line[i] == "^" and laser_count[i] > 0:
            laser_count[i - 1] += laser_count[i]
            laser_count[i + 1] += laser_count[i]
            laser_count[i] = 0
    print(laser_count)

print(sum(laser_count))