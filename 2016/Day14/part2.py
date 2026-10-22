import hashlib
import re

def stretched_hash(index):
    if index in cache:
        return cache[index]

    h = hashlib.md5((salt + str(index)).encode()).hexdigest()
    for i in range(2016):
        h = hashlib.md5(h.encode()).hexdigest()

    cache[index] = h
    return h

salt = "cuanljph"
index = 0
keys_found = 0
cache = {}

pattern = r'(.)\1{2}'
while True:

    current_hash = stretched_hash(index)
    match = re.search(pattern, current_hash)
    if match:
        next_to_find = match.group()[0] * 5
        for j in range(index + 1, index + 1001):
            future_hash = stretched_hash(j)
            if next_to_find in future_hash:
                keys_found += 1
                print(f"Key found! Total found {keys_found} keys")
                break
        if keys_found == 64:
            break
    index += 1
print(index)

