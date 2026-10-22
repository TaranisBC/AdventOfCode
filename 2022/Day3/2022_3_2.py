with open("puzzle3.txt", "r") as puzzle_input:
	lsItems = puzzle_input.read().splitlines()

priority_order = (".abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
lsPriority = []


for i in range (0, len(lsItems), 3):
	bag1 = lsItems[i]
	bag2 = lsItems[i+1]
	bag3 = lsItems[i+2]
	for char in bag1:
		if char in bag2 and char in bag3:
			lsPriority.append(priority_order.index(char))
			break

print(sum(lsPriority))