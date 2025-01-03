import sys

if len(sys.argv) >= 2 and sys.argv[1] == '-s':
    filename = 'day7/sample.txt'
else:
    filename = 'day7/input.txt'

input = open(filename, 'r')
eq = [(int(x), [int(n) for n in y.strip().split()]) for (x,y) in [each.split(':') for each in input.readlines()]]

def is_calibrated(total, partial, i, nums):
    if i == len(nums):
        return partial == total
    elif partial <= total:
        return is_calibrated(total, partial * nums[i], i+1, nums) or is_calibrated(total, partial + nums[i], i+1, nums)
    return False
 

result = 0
for each in eq:
    if is_calibrated(each[0], each[1][0], 1, each[1]):
        result = result + each[0]

print("part 1:", result)

def is_calibrated2(total, partial, i, nums):
    if i == len(nums):
        return partial == total
    elif partial <= total:
        return is_calibrated2(total, partial * nums[i], i+1, nums) or \
            is_calibrated2(total, partial + nums[i], i+1, nums) or \
            is_calibrated2(total, int(str(partial) + str(nums[i])), i+1, nums)
    return False

result = 0
for each in eq:
    if is_calibrated2(each[0], each[1][0], 1, each[1]):
        result = result + each[0]

print("part 2:", result)
