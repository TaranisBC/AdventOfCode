with open ("puzzle1.txt", "r") as puzzle_input:
	lsElves = puzzle_input.read().split("\n\n")

lsCalories = []

for elf in lsElves:
	calories = []
	calories = (elf.split("\n"))
	total_calories = 0
	for element in calories:
		total_calories += int(element)
		lsCalories.append(total_calories)
	

print(max(lsCalories))
