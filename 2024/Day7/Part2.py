import itertools
import time

def generate_sign_combinations(n: int):
    combinations = list(itertools.product(["+", "*", "||"], repeat=n))
    return combinations

def evaluate_list(oper_list: list[str]):
    oper_string = f"{oper_list[0]} {oper_list[1]} {oper_list[2]}"
    if "||" in oper_string:
        result = oper_list[0] + oper_list[2]
    else:
        result = eval(oper_string)
    for i in range(3):
        oper_list.pop(0)
    oper_list.insert(0, str(result))
    if len(oper_list) == 1:
        return result
    else:
        return(evaluate_list(oper_list))


if __name__ == '__main__':    

    with open("/home/bruno/DataDrive/adventofcode/2024/Day7/input.txt", "r") as puzzle:
        values = puzzle.read().splitlines()    

    calibration_values = []
    operations = []

    sum_valid_values = 0
    

    for value in values:
        calib, oper = value.split(": ")
        calibration_values.append(calib)
        operations.append(oper.split(" "))

    for i in range(0, len(operations)):        
        operator_combos = generate_sign_combinations(len(operations[i]) - 1)
        for combo in operator_combos:
            operation_list = []
            for j in range (0, len(combo)):
                operation_list.append(operations[i][j])
                operation_list.append(combo[j])
            operation_list.append(operations[i][-1])
            final_result = evaluate_list(operation_list)
            if int(final_result) == int(calibration_values[i]):                
                sum_valid_values += int(calibration_values[i])
                break

    print(sum_valid_values)            


