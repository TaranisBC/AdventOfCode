def read_and_format_data() -> list[list[int]]:
    with open("input.txt", "r") as puzzle:
        values = puzzle.read().splitlines()

    left_values = []
    right_values = []
    for line in values:
        splitted = line.split("   ")
        left_values.append(int(splitted[0]))
        right_values.append(int(splitted[1]))

    return[left_values, right_values]


def solve_part_1(left_values: list[int], right_values: list[int]):
    left_values.sort()
    right_values.sort()

    distance = 0

    for i in range(len(left_values)):
        distance += abs(left_values[i] - right_values[i])

    print(distance)
    

def solve_part_2(left_values: list[int], right_values: list[int]):
    score = 0

    for value in left_values:
        score += value * right_values.count(value)

    print(score)      

if __name__ == '__main__':

    problem_data = read_and_format_data()

    left = problem_data[0]
    right = problem_data[1]

    solve_part_1(left, right)
    solve_part_2(left, right)