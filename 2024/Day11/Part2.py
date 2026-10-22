import time

def perform_blink(stone: str) -> list[str]:
    final_stones = []
    if len(stone) % 2 == 0:
        split_index = int(len(stone) / 2)
        new_stone_1 = stone[0: split_index]
        new_stone_2 = (stone[split_index:]).lstrip("0")
        final_stones.append(new_stone_1)
        if new_stone_2 == "":
            new_stone_2 = "0"
        final_stones.append(new_stone_2)
    elif stone == "0":
        final_stones.append("1")
    else:
        new_stone = str(int(stone) * 2024)
        final_stones.append(new_stone)
    return final_stones

if __name__ == '__main__':
    start = time.time()

    with open("input.txt", "r") as puzzle:
        arrangement = puzzle.read()

    stones = arrangement.split(" ")

    stone_dict = {}

    for stone in stones:
        if stone in stone_dict:
            stone_dict[stone] += 1
        else:
            stone_dict[stone] = 1

    print(stone_dict)

    blinks = 0
    while blinks < 75:
        blinks += 1
        new_dict = {}
        for key, value in stone_dict.items():
            new_stones = perform_blink(key)
            for stn in new_stones:
                if stn in new_dict:
                    new_dict[stn] += value
                else:
                    new_dict[stn] = value
        stone_dict = new_dict.copy()

    sum = 0
    for element in stone_dict.values():
        sum += element

    print(sum)    

    end = time.time()

    print(f"{(end-start) * 1000} ms")