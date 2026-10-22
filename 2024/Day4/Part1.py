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
        if values[i][j] == "X":
            # Check up
            if values[i-1][j] == "M" and values[i-2][j] == "A" and values[i-3][j] == "S":
                xmas_count += 1
            
            #Check down
            if values[i+1][j] == "M" and values[i+2][j] == "A" and values[i+3][j] == "S":
                xmas_count += 1
            
            # Check left
            if values[i][j-1] == "M" and values[i][j-2] == "A" and values[i][j-3] == "S":
                xmas_count += 1

            # Check right
            if values[i][j+1] == "M" and values[i][j+2] == "A" and values[i][j+3] == "S":
                xmas_count += 1
            
            # Check diagonal up left
            if values[i-1][j-1] == "M" and values[i-2][j-2] == "A" and values[i-3][j-3] == "S":
                xmas_count += 1
            
            # Check diagonal down left
            if values[i+1][j-1] == "M" and values[i+2][j-2] == "A" and values[i+3][j-3] == "S":
                xmas_count += 1

            # Check diagonal up right            
            if values[i-1][j+1] == "M" and values[i-2][j+2] == "A" and values[i-3][j+3] == "S":
                xmas_count += 1

            # Check diagonal down right
            if values[i+1][j+1] == "M" and values[i+2][j+2] == "A" and values[i+3][j+3] == "S":
                xmas_count += 1
    
print(xmas_count)