with open("puzzle3.txt", "r") as puzzle_input:
	lsItems = puzzle_input.read().splitlines()

priority_order = (".abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
lsPriority = []

for item in lsItems:
	middle = len(item) // 2	
	left_side = item[:middle]
	right_side = item[middle:]
	print(len(left_side))
	print(len(right_side))
	for char in left_side:
		if char in right_side:
			lsPriority.append(priority_order.index(char))
			break

print(sum(lsPriority))