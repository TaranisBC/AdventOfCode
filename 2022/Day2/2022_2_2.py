with open ("puzzle2.txt", "r") as puzzle_input:
	lsRounds = puzzle_input.read().splitlines()

dict  = {
	'AX' : 3,
	'AY' : 4,
	'AZ' : 8,
	'BX' : 1,
	'BY' : 5,
	'BZ' : 9,
	'CX' : 2,
	'CY' : 6,
	'CZ' : 7
}

total = 0
for element in lsRounds:
	new_element = element[0] + element [2]
	total += dict[new_element]

print(total)

