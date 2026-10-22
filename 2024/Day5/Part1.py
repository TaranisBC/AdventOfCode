with open("/home/bruno/DataDrive/adventofcode/2024/Day5/input.txt", "r") as puzzle:
    values = puzzle.read().splitlines()

index_to_split = values.index("")
instruction_list = values[0:index_to_split]
pages_to_print_list = values[index_to_split + 1:]

inst_dict = {}

for instruction in instruction_list:
    details = instruction.split('|')    
    if details[0] in inst_dict:
        inst_dict[details[0]].append(details[1])
    else:
        inst_dict[details[0]] = [details[1]]

valid_instructions = []

for prints in pages_to_print_list:
    valid = True
    pages = prints.split(",")
    for i in range(1, len(pages)):
        if pages[i] in inst_dict.keys():
            required_order = inst_dict[pages[i]]
            pages_to_check = pages[0:i]
            for page in pages_to_check:
                if page in required_order:
                    valid = False
                    break
            if valid == False:                
                break
    if valid:
        valid_instructions.append(pages)

middle_sum = 0
for inst in valid_instructions:
    middle_sum += int(inst[len(inst) // 2])

print(middle_sum)