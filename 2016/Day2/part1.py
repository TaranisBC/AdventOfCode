with open("input.txt") as f:
    data = f.read().splitlines()

print(data)

code = ""
keypad = [
    ["1", "2", "3"],
    ["4", "5", "6"],
    ["7", "8", "9"]
]

x_pos = 1
y_pos = 1

for line in data:
    for i in range(len(line)):
        if line[i] == "U" and y_pos > 0 :
            y_pos -= 1
        elif line[i] == "D" and y_pos < 2 :
            y_pos += 1
        elif line[i] == "R" and x_pos < 2 :
            x_pos += 1
        elif line[i] == "L" and x_pos > 0 :
            x_pos -= 1

    digit = keypad[y_pos][x_pos]
    code += digit

print(code)


