with open("puzzle6.txt", "r") as puzzle_input:
	packet = puzzle_input.read()

for i in range(13, len(packet), 1):
	header = packet[i-13:i+1]
	checkset = set(header)
	if len(checkset) == 14:
		print(i + 1)
		break

