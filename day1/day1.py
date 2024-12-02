#!/usr/bin/env python3

import sys
if len(sys.argv) >= 2 and sys.argv[1] == '-s':
    input = open('sample.txt', 'r')
else:
    input = open('input.txt', 'r')

pairs = [each.rstrip('\n').split() for each in input.readlines()]
left = sorted([int(each[0]) for each in pairs])
right = sorted([int(each[1]) for each in pairs])

print("part 1:", sum(map(lambda each: abs(each[0] - each[1]), zip(left, right))))
print("part 2:", sum(map(lambda each: each * right.count(each), left)))
