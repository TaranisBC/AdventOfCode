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

invalid_instructions = []

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
                invalid_instructions.append(pages)
                break     

valid_inst = []      

for instruction in invalid_instructions:
    valid = False    
    while valid == False:  
        restart = False      
        for i in range(1, len(instruction)):

            if instruction[i] in inst_dict.keys():
                required_order = inst_dict[instruction[i]]
                pages_to_check = instruction[0:i]
                for j in range(len(pages_to_check)):
                    if pages_to_check[j] in required_order:
                        valid = False
                        page_to_move = instruction.pop(i)
                        instruction.insert(j, page_to_move)
                        restart = True                   
                        break
                if i == len(instruction) - 1:
                    valid = True
                    valid_inst.append(instruction)
                    break
                if restart:
                    break


print(valid_inst)

middle_sum = 0
for inst in valid_inst:
    middle_sum += int(inst[len(inst) // 2])

print(middle_sum)