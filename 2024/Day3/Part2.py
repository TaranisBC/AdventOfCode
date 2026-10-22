import re

with open("/home/bruno/DataDrive/adventofcode/2024/Day3/input.txt", "r") as puzzle:
    values = puzzle.read()

print(values)

pattern = r"mul\(\d{1,3},\d{1,3}\)|do\(\)|don't\(\)"

matches = re.findall(pattern, values)

enabled = True
sum = 0

for result in matches:
    if result == "do()":
        enabled = True
    elif result == "don't()":
        enabled = False
    else:
        if enabled:
            val = result[4:len(result)-1]
            numbers = val.split(',')
            sum += int(numbers[0]) * int(numbers[1])

print(sum)