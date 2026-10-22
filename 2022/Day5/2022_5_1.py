crates_positions = [
["F","C","J","P","H","T","W"],
["G","R","V","F","Z","J","B","H"],
["H","P","T","R"],
["Z","S","N","P","H","T"],
["N","V","F","Z","H","J","C","D"],
["P","M","G","F","W","D","Z"],
["M","V","Z","W","S","J","D","P"],
["N","D","S"],
["D","Z","S","F","M"]
]

with open ("puzzle5.txt","r") as puzzle_input:
	lsinstructions = puzzle_input.read().splitlines()

lsDetailedInstructions = []

for element in lsinstructions:
	lsDetailedInstructions.append(element.split(" "))

#1,3,5
for instruction in lsDetailedInstructions:
	nb_to_move = int(instruction[1])
	init_stack = int(instruction[3]) - 1
	final_stack = int(instruction[5]) - 1

	for i in range(0, nb_to_move, 1):
		crates_positions[final_stack].append(crates_positions[init_stack].pop())

message = ""
for element in crates_positions:
	message += (element.pop())

print(message)
