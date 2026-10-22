import math

def get_cephalopod_numbres(original_numbers: list[str]) -> list[int]:
    cephalopod_numbers = []
    for i in range(len(original_numbers[0])):
        new_number = ""
        for j in range(len(original_numbers)):
            if original_numbers[j][i] != "0":
                 new_number += original_numbers[j][i]
        if new_number != "":
            cephalopod_numbers.append(int(new_number))
    return cephalopod_numbers


with open("input.txt", "r") as f:
    lines = f.readlines()

operators = [x for x in lines.pop() if x != " "]

maxlen = max(len(l) for l in lines)
lines = [l.ljust(maxlen) for l in lines]


columns = []
in_col = False
start = 0

columns = []
in_col = False
start = 0

for i in range(maxlen):
    # Regarder verticalement s'il y a des nombres ou si c'est une colonne d'espace complète (point de séparation des nombres)
    if any(line[i].isdigit() for line in lines):
        if not in_col:
            in_col = True
            start = i
    else:
        if in_col:
            in_col = False
            # Trouve les délimiteurs de chaque colonne -> indice de début et de fin
            columns.append((start, i))

# Ajouter le dernier nombre qui n'est pas couvert par l'algo précédent (ne verra jamais la position de fin)
if in_col:
    columns.append((start, maxlen))


col_values = []
for col in columns:
    current_col = []
    for line in lines:
        # Extraire le nombre et ajouter les 0 nécessaires
        number = line[col[0]:col[1]]
        while " " in number:
            number = number.replace(" ", "0")
        current_col.append(number)
    col_values.append(current_col)

results = []
for i in range(len(operators)):
    c_numbers = get_cephalopod_numbres(col_values[i])
    if operators[i] == "+":
        results.append(sum(c_numbers))
    else:
        results.append(math.prod(c_numbers))

print(sum(results))