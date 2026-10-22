import pandas as pd

with open("input.txt", "r") as f:
    lines = f.readlines()

operators = [x for x in lines.pop() if x != " "]

int_lines = []
for line in lines:
    new_line = [int(x.strip()) for x in line.split(" ") if x != ""]
    int_lines.append(new_line)

df = pd.DataFrame(int_lines)

results = []
for i in range(len(operators)):
    if operators[i] == "+":
        results.append(df[i].sum())
    else:
        results.append(df[i].prod())

print(sum(results))