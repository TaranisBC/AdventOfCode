with open("input.txt", "r") as f:
    data = f.read().splitlines()

deltas = [int(line) for line in data]

frequency = 0
known_frequencies = {0}
while True:
    frequency_found = False
    for delta in deltas:
        frequency += delta
        if frequency in known_frequencies:
            frequency_found = True
            print(frequency)
            break
        else:
            known_frequencies.add(frequency)
    if frequency_found:
        break