import hashlib

input_string = "ugkcyxxp"
index = 0
password = "********"
print(password)
while True:
    test = input_string + str(index)
    current_hash = hashlib.md5(test.encode()).hexdigest()
    if current_hash.startswith("00000"):
        position = current_hash[5]
        if position in "01234567":
            if password[int(position)] == "*":
                password = password[:int(position)] + current_hash[6] + password[int(position)+1:]
                print(password)
    index += 1

    if "*" not in password:
        break

print(password)