with open ("puzzle2.txt", "r") as puzzle_input:
	lsRounds = puzzle_input.read().splitlines()

dict  = {
	'AX' : 4,
	'AY' : 8,
	'AZ' : 3,
	'BX' : 1,
	'BY' : 5,
	'BZ' : 9,
	'CX' : 7,
	'CY' : 2,
	'CZ' : 6
}

total = 0
for element in lsRounds:
	new_element = element[0] + element [2]
	total += dict[new_element]

print(total)

