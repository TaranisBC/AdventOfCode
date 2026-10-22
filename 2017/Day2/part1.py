with open("input.txt", "r") as f:
    lines = f.read().splitlines()

somme = 0

for line in lines:
    data = [int(x) for x in line.split()]
    somme += (max(data) - min(data))

print(somme)