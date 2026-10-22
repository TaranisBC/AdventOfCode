import re

with open("input.txt") as f:
    data = f.read().splitlines()

ssl_addresses = 0

aba_look = re.compile(r'(?=(([a-z])(?!\2)([a-z])\2))')  # uses backreference \2 inside lookahead

for line in data:
    outside = re.findall(r'([a-z]+)(?:\[|$)', line + "[")
    inside  = re.findall(r'\[([a-z]+)\]', line)

    matches_outside = []
    for part in outside:
        for m in aba_look.finditer(part):
            matches_outside.append(m.group(1))

    found_ssl = False
    for aba in matches_outside:
        bab = aba[1] + aba[0] + aba[1]
        if any(bab in part for part in inside):
            found_ssl = True
            break

    if found_ssl:
        ssl_addresses += 1

print(ssl_addresses)
