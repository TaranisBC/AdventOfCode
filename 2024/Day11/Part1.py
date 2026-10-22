import time

start = time.time()

with open("input.txt", "r") as puzzle:
    arrangement = puzzle.read()

stones = arrangement.split(" ")
blinks = 0
while blinks < 25:
    blinks += 1    
    final_stones = []
    for stone in stones:
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
    stones = final_stones.copy()    

print(len(stones))   
end = time.time()

print((end - start) * 1000)