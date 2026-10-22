with open("input.txt", "r") as f:
    data = f.read().splitlines()

directions = [step[0] for step in data]
movement = [int(step[1:]) for step in data]

position = 50
password = 0

for i in range(len(movement)):
    tours_complets = movement[i] // 100
    deplacement = movement[i] % 100
    password += tours_complets
    if directions[i] == "L":
        if position == 0:
            position = position - deplacement + 100
        else:
            position -= deplacement
            if position < 0:
                position += 100
                password += 1
            elif position == 0:
                password += 1
    else:
        if position == 0:
            position += deplacement
        else:
            position += deplacement
            if position > 99:
                position -= 100
                password += 1


print(password)