import sys

if len(sys.argv) >= 2 and sys.argv[1] == '-s':
    filename = 'sample.txt'
else:
    filename = 'input.txt'

input = open(filename, 'r')
reports = [list(map(lambda n: int(n), each.strip().split())) for each in input.readlines()]

def is_safe(report):
    diffs = [cur - report[prev_idx] for prev_idx, cur in enumerate(report[1:])]
    return all(map(lambda n: n in [1, 2, 3], diffs)) or all(map(lambda n: n in [-1, -2, -3], diffs))

print("part 1:", sum(map(is_safe, reports)))

def is_safe2(report):
    if is_safe(report):
        return True
    for i in range(len(report)):
        tmp = report.copy()
        tmp.pop(i)
        if is_safe(tmp):
            return True
    return False

print("part 2:", sum(map(is_safe2, reports)))
