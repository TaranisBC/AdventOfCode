with open("puzzle4.txt", "r") as puzzle_input:
    lsInput = puzzle_input.read().splitlines()

overlap_counter = 0

for element in lsInput:
    elementAB = element.split(",")
    print(elementAB)
    dash1_index = elementAB[0].index("-")
    dash2_index = elementAB[1].index("-")

    element_A_start = int(elementAB[0][:dash1_index])
    element_A_end = int(elementAB[0][dash1_index + 1:])

    element_B_start = int(elementAB[1][:dash2_index])
    element_B_end = int(elementAB[1][dash2_index + 1:])

    if ((element_A_start >= element_B_start) and (element_A_end <= element_B_end)) or (
            (element_B_start >= element_A_start) and (element_B_end <= element_A_end)) or (
            (element_A_start <= element_B_start) and (element_A_end >= element_B_start)) or (
             (element_B_start <= element_A_start) and (element_B_end >= element_A_start)) :
        overlap_counter += 1

print(overlap_counter)
