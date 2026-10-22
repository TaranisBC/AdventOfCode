import hashlib

input_string = "ugkcyxxp"
index = 0
password = ""
while True:
    test = input_string + str(index)
    current_hash = hashlib.md5(test.encode()).hexdigest()
    if current_hash.startswith("00000"):
        password += current_hash[5]
    index += 1

    if len(password) == 8:
        break

print(password)