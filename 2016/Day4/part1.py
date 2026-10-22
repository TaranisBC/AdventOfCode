def verify_room(room: str) -> int:
    # Split room from checksum
    delimiter_index = room.index('[')
    checksum = room[delimiter_index + 1 :-1]

    room_code = room[:delimiter_index]

    sector_delimiter_index = room_code.rfind('-')
    sector_code = room_code[sector_delimiter_index + 1:]

    room_code = room_code[:sector_delimiter_index]

    characters_in_code = set(room_code)

    char_count = {}
    for character in characters_in_code:
        count = room_code.count(character)
        char_count[character] = count

    del char_count['-']
    sorted_chars = sorted(char_count.items(), key=lambda x: (-x[1],x[0]))

    room_checksum = ""
    for i in range(5):
        room_checksum += sorted_chars[i][0]

    if room_checksum == checksum:
        return int(sector_code)
    else:
        return 0


with open("input.txt") as f:
    data = f.read().splitlines()

sector_sum = 0

for line in data:
    sector_sum += verify_room(line)

print(sector_sum)