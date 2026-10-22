import re

with open("/home/bruno/DataDrive/adventofcode/2024/Day3/input.txt", "r") as puzzle:
    values = puzzle.read()

print(values)

pattern = r"mul\(\d{1,3},\d{1,3}\)"

matches = re.findall(pattern, values)

vals = []

for result in matches:
    vals.append(result[4:len(result) -1])

print(vals)

sum = 0

for val in vals:
    numbers = val.split(',')
    sum += int(numbers[0]) * int(numbers[1])

print(sum)