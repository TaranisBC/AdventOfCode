import time
with open("input.txt", "r") as file:
    instructions = file.read().splitlines()

registries = {
    "a": 7,
    "b": 0,
    "c": 0,
    "d": 0,
}

i = 0
total_steps = 0
while i < len(instructions):
    print(registries)
    print(i)
    total_steps += 1
    print(total_steps)
    current_instruction = instructions[i].split(" ")
    match current_instruction[0]:
        case "cpy":
            if current_instruction[1] in registries.keys():
                value = registries[current_instruction[1]]
                registries[current_instruction[2]] = value
            else:
                registries[current_instruction[2]] = int(current_instruction[1])
            i += 1
        case "inc":
            registries[current_instruction[1]] += 1
            i += 1
        case "dec":
            if registries[current_instruction[1]] > 0:
                registries[current_instruction[1]] -= 1
            i += 1
        case "jnz":
            if current_instruction[1] not in ["a", "b", "c", "d"]:
                if int(current_instruction[1]) != 0:
                    try:
                        i += int(registries[current_instruction[2]])
                    except ValueError:
                        i += 1
            else:
                if registries[current_instruction[1]] != 0:
                    i += int(current_instruction[2])
                else:
                    i += 1
        case "tgl":
            print("Toggle")
            try:
                delta = int(registries[current_instruction[1]])
                j = i + delta
                if j < len(instructions):
                    toggled = instructions[j]
                    full_set = toggled.split(" ")
                    # One argument instructions
                    if len(full_set) == 2:
                        if full_set[0] == "inc":
                            full_set[0] = "dec"
                        else:
                            full_set[0] = "inc"

                    # Two argument instructions
                    elif len(full_set) == 3:
                        if full_set[0] == "jnz":
                            full_set[0] = "cpy"
                        else:
                            full_set[0] = "jnz"

                    new_instruction_line = " ".join(full_set)
                    instructions[j] = new_instruction_line
            except ValueError:
                print("invalid")
            i += 1





print(registries["a"])