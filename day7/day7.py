import sys

if len(sys.argv) >= 2 and sys.argv[1] == '-s':
    filename = 'day7/sample.txt'
else:
    filename = 'day7/input.txt'

input = open(filename, 'r')
eqs = [(int(x), [int(n) for n in y.strip().split()]) for (x,y) in [each.split(':') for each in input.readlines()]]

def validate(total, partial, i, nums, concat=False):
    if i == 0:
        return validate(total, nums[i], i+1, nums, concat)
    elif i == len(nums) and partial == total:
        return total
    elif i == len(nums):
        return 0
    elif concat and partial <= total:
        return validate(total, partial * nums[i], i+1, nums, concat) or \
            validate(total, partial + nums[i], i+1, nums, concat) or \
            validate(total, int(str(partial) + str(nums[i])), i+1, nums, concat)
    elif partial <= total:
        return validate(total, partial * nums[i], i+1, nums) or \
            validate(total, partial + nums[i], i+1, nums)
    return 0

def calibrated(eq):
    return validate(eq[0], -1, 0, eq[1])

def calibrated2(eq):
    return validate(eq[0], -1, 0, eq[1], concat=True)

print("part 1:", sum(map(calibrated, eqs)))
print("part 2:", sum(map(calibrated2, eqs)))
