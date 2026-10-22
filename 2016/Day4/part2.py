def verify_room(room: str) -> list[str]:
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
        return [room_code, sector_code]
    else:
        return ["", ""]

with open("input.txt") as f:
    data = f.read().splitlines()


characters = 'abcdefghijklmnopqrstuvwxyz'

for line in data:
    test_case = verify_room(line)
    if test_case[0] != "":
        rot = int(test_case[1]) % 26
        final_string = ""
        for character in test_case[0]:
            if character == "-":
                final_string += " "
            else:
                initial_index = characters.index(character)
                final_index = initial_index + rot
                if final_index > 25:
                    final_index -= 26

                final_string += characters[final_index]
        with open("output.txt", "a") as f:
            f.write(final_string + " " + test_case[1] + "\n")

