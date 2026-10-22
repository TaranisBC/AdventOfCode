with open("puzzle6.txt", "r") as puzzle_input:
	packet = puzzle_input.read()

for i in range(3, len(packet), 1):
	header = packet[i-3:i+1]
	checkset = set(header)
	if len(checkset) == 4:
		print(i + 1)
		break

