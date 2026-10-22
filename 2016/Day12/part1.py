with open("input.txt", "r") as file:
    instructions = file.read().splitlines()

registries = {
    "a": 0,
    "b": 0,
    "c": 1,
    "d": 0,
}

i = 0
while i < len(instructions):
    print(registries)
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
                if int(current_instruction[1]) > 0:
                    i += int(current_instruction[2])
            else:
                if registries[current_instruction[1]] > 0:
                    i += int(current_instruction[2])
                else:
                    i += 1



print(registries["a"])