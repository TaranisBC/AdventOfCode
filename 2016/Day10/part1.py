with open("input.txt", "r") as file:
    data = file.read().splitlines()

initial_values = []

for line in data:
    if "value" in line:
        data.pop(data.index(line))
        initial_values.append(line)


bots = {}
outputs = {}

for line in initial_values:
    instructions = line.split(" ")
    value = int(instructions[1])
    bot = instructions[5]

    if bot not in bots.keys():
        bots[bot] = [int(value)]
    else:
        bots[bot].append(int(value))

bot_number = 0
while True:
    for key, value in bots.items():
        bot_added = False
        if len(value) == 2:
            if sorted(value) == [17, 61]:
                bot_number = key
                break

            ordered = sorted(value)
            low, high = ordered[0], ordered[1]
            bots[key] = []

            for line in data:
                if f"bot {key} gives" in line:
                    bot_instructions = line.split(" ")
                    if bot_instructions[6] not in bots.keys():
                        bots[bot_instructions[6]] = [low]
                        bot_added = True
                    else:
                        bots[bot_instructions[6]].append(low)

                    if bot_instructions[11] not in bots.keys():
                        bots[bot_instructions[11]] = [high]
                        bot_added = True
                    else:
                        bots[bot_instructions[11]].append(high)

                    print(f"Bot {bot_instructions[6]} recieved {low}")
                    print(f"Bot {bot_instructions[11]} recieved {high}")
        if bot_added:
            break

