import re

with open("input.txt") as f:
    data = f.read().splitlines()


tls_addresses = 0
for line in data:
    # Extract sequences outside of brackets
    outside = re.findall(r'([a-z]+)(?:\[|$)', line + "[")  # add "[" to make last part match
    # Extract sequences inside brackets
    inside = re.findall(r'\[([a-z]+)\]', line)

    abba_pattern = re.compile(r'([a-z])(?!\1)([a-z])\2\1')

    outside_matches = [part for part in outside if re.search(abba_pattern, part)]
    inside_matches = [part for part in inside if re.search(abba_pattern, part)]

    if len(outside_matches) > 0 and len(inside_matches) == 0:
        tls_addresses += 1

print(tls_addresses)