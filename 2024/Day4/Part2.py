with open("input.txt", "r") as puzzle:
    values = puzzle.read().splitlines()

for i in range(3):
    values.append("*" * len(values[0])) 
    values.insert(0,"*" * len(values[0]))

for i in range(len(values)):
    values[i] = "***" + values[i] + "***"

xmas_count = 0

for i in range(3, len(values) - 3):
    for j in range(3, len(values[0]) -3):
        if values[i][j] == "A":
            # Check Ms on top
            if values[i-1][j-1] == "M" and values[i-1][j+1] == "M" and values[i+1][j-1] == "S" and values[i+1][j+1] == "S" :
                xmas_count += 1

            # Check Ms on left
            if values[i-1][j-1] == "M" and values[i+1][j-1] == "M" and values[i+1][j+1] == "S" and values[i-1][j+1] == "S" :
                xmas_count += 1

            # Check Ms on right
            if values[i-1][j+1] == "M" and values[i+1][j+1] == "M" and values[i+1][j-1] == "S" and values[i-1][j-1] == "S" :
                xmas_count += 1

            # Check Ms on bottom
            if values[i+1][j-1] == "M" and values[i+1][j+1] == "M" and values[i-1][j+1] == "S" and values[i-1][j-1] == "S" :
                xmas_count += 1
    
print(xmas_count)