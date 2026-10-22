with open("input.txt", "r") as f:
    data = f.read().splitlines()

directions = [step[0] for step in data]
movement = [int(step[1:]) for step in data]

position = 50
password = 0

for i in range(len(movement)):
    deplacement = movement[i] % 100
    if directions[i] == "L":
       position -= deplacement
       if position < 0:
           position += 100
    else:
        position += deplacement
        if position > 99:
            position -= 100
    if position == 0:
        password += 1

print(password)