with open("input.txt", "r") as f:
    lines = f.read().splitlines()

somme = 0

for line in lines:
    data = [int(x) for x in line.split()]
    for i in range(len(data) -1 ):
        paire_trouvee = False
        for j in range(i+1, len(data)):
            if data[i] % data[j] == 0 or data[j] % data[i] == 0:
                if data[j] > data[i] :
                    somme += data[j] // data[i]
                else:
                    somme += data[i] // data[j]
                paire_trouvee = True
                break
        if paire_trouvee:
            break

print(somme)