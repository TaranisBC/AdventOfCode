import time

class Disc:
    def __init__(self, current_position, total_position ):
        self.current_position = current_position
        self.total_position = total_position

discs = [
    Disc(15, 17),
    Disc(2, 3),
    Disc(4, 19),
    Disc(2, 13),
    Disc(2, 7),
    Disc(0, 5)
]

current_time = 0
while True:
    found = False
    current_time += 1
    final_positions = []
    for disc in discs:
        position = disc.current_position + (current_time % disc.total_position)
        if position >= disc.total_position:
            position -= disc.total_position
        final_positions.append(position)
    print(final_positions)
    if final_positions == [16,  1, 16, 9, 2, 4]:
        print(current_time)
        break


