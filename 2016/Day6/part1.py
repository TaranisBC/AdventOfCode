from collections import Counter
from typing import Collection

with open("input.txt") as f:
    data = f.read().splitlines()

result = list(zip(*data))

# If you want them as lists (not tuples):
result = [list(group) for group in result]

corrected = ""
for group in result:
    joined = "".join(group)
    print(Counter(joined))


print(corrected)