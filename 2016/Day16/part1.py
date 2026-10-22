def dragon_curve(data: str) -> str:
    a = data
    b = data[::-1]
    inverse_b = ""
    for char in b:
        if char == "1":
            inverse_b += "0"
        elif char == "0":
            inverse_b += "1"

    return a + "0" + inverse_b

def calculate_checksum(data):
    checksum = ""
    for i in range(0, len(data), 2):
        if data[i] != data[i + 1]:
            checksum += "0"
        else:
            checksum += "1"
    if len(checksum) % 2 == 0:
        return calculate_checksum(checksum)
    else:
        return checksum

disk_space = 35651584
initial_data = "00101000101111010"

while len(initial_data) < disk_space:
    initial_data = dragon_curve(initial_data)
    print(len(initial_data))

disk_data = initial_data[0:disk_space]

print(calculate_checksum(disk_data))


