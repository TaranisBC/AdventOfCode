def evaluate_safe_report(tested_report: list[int]) -> int:
    """
    Function that takes a reoport to test and checks for errors. If an error is found, the index of the level causing
    the error is returned. If the report is safe -1 is returned.
    :param tested_report: The report to test
    :return: The integer of the first level causing an error OR -1 if the report is safe
    """
    if tested_report[0] > tested_report [1]:        
        for i in range(1, len(tested_report)):
            difference = abs(tested_report[i] - tested_report[i-1])
            if tested_report[i] > tested_report[i - 1] or difference < 1 or difference > 3:                
                return i
    else:
        for i in range(1, len(tested_report)):
            difference = abs(tested_report[i] - tested_report[i-1])
            if tested_report[i] < tested_report[i - 1] or difference < 1 or difference > 3:
                return i
    return -1

if __name__ == '__main__':

    with open("input.txt", "r") as puzzle:
        values = puzzle.read().splitlines()

    reports = [list(map(int, s.split())) for s in values]

    safe_reports = 0

    for report in reports:
        if report[0] == report[1] and report[1] == report[2]:
            pass
        else:
            is_safe = evaluate_safe_report(report)
            if is_safe == -1:
                safe_reports += 1                             
            else:
                for i in range(len(report)):
                    test_report = report.copy()
                    test_report.pop(i)
                    is_safe = evaluate_safe_report(test_report)
                    if is_safe == -1:
                        safe_reports += 1                    
                        break            
                                        

    print(safe_reports)