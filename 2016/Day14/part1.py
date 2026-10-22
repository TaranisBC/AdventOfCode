import hashlib
import re

salt = "cuanljph"
index = 0
keys_found = 0
cache = {}

pattern = r'(.)\1{2}'
while True:

    current_hash = ""
    if index in cache:
        current_hash = cache[index]
    else:
        current_hash = hashlib.md5((salt + str(index)).encode()).hexdigest()
    match = re.search(pattern, current_hash)
    if match:
        next_to_find = match.group()[0] * 5
        for j in range(index + 1, index + 1001):
            future_hash = hashlib.md5((salt + str(j)).encode()).hexdigest()
            cache[j] = future_hash
            if next_to_find in future_hash:
                keys_found += 1
                print(f"Key found! Total found {keys_found} keys")
                break
        if keys_found == 64:
            break
    index += 1
print(index)

