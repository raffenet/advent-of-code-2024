#!/usr/bin/env python3

import sys
if len(sys.argv) >= 2 and sys.argv[1] == '-s':
    input = open('sample.txt', 'r')
else:
    input = open('input.txt', 'r')

pairs = [each.rstrip('\n').split() for each in input.readlines()]
left = [int(each[0]) for each in pairs]
right = [int(each[1]) for each in pairs]
left.sort()
right.sort()

total = 0
for each in zip(left, right):
    total += abs(each[0] - each[1])
print("part 1:", total)

similarity_score = 0
for each in left:
    similarity_score += each * right.count(each)
print("part 2:", similarity_score)
