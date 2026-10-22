with open("input.txt", "r") as f:
    lines = f.read().splitlines()

supported_programs = []

for line in lines:
    if " -> " in line:
        segments = line.split(" -> ")
        programs = segments[1].split(", ")
        for program in programs:
            supported_programs.append(program)

for line in lines:
    full_data = line.split(" ")
    if full_data[0] not in supported_programs:
        print(full_data[0])
        break
