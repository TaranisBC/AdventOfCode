with open("input.txt", "r") as f:
    data = f.read().splitlines()

matching_pair= ()

for i in range(len(data)-1):
    pair_found = False
    for j in range(i+1, len(data)):
        matching_positions = 0
        for c1, c2 in zip(data[i], data[j]):
            if c1 == c2:
                matching_positions += 1

        if matching_positions == len(data[i]) - 1:
            matching_pair = (i, j)
            break
    if pair_found:
        break

pos_to_remove = 0
ind = 0
for c1, c2 in zip(data[matching_pair[0]], data[matching_pair[1]]):
    if c1 != c2:
        pos_to_remove = ind
        break
    ind += 1

print(pos_to_remove)
resultat = data[matching_pair[0]][0:pos_to_remove] + data[matching_pair[1]][pos_to_remove + 1:]
print(resultat)


