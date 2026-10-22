with open("input.txt", "r") as f:
    passphrases = f.read().splitlines()

valid_passphrases = []

for passphrase in passphrases:
    words = passphrase.split(" ")
    if len(words) == len(set(words)):
        valid_passphrases.append(passphrase)

print(len(valid_passphrases))

### PART 2 STARTS HERE

secure_valid_passpharses = []
for passphrase in valid_passphrases:
    valid = True
    words = passphrase.split(" ")
    for i in range(len(words) - 1):
        for j in range(i + 1, len(words)):
            if sorted(list(words[i])) == sorted(list(words[j])):
                valid = False
                break
        if not valid:
            break
    if valid:
        secure_valid_passpharses.append(passphrase)

print(len(secure_valid_passpharses))
