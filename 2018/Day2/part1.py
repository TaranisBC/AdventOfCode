with open("input.txt", "r") as f:
    data = f.read().splitlines()

double_letters = 0
triple_letters = 0


for line in data:
    freq = {}
    for c in line:
        if c in freq:
            freq[c] += 1
        else:
            freq[c] = 1

    if 2 in freq.values():
        double_letters += 1
    if 3 in freq.values():
        triple_letters += 1

print(double_letters * triple_letters)