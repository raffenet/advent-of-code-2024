#!/usr/bin/env python3
import sys
if len(sys.argv) >= 2 and sys.argv[1] == '-s':
    input = open('sample.txt', 'r')
else:
    input = open('input.txt', 'r')

left = [int(each.rstrip('\n').split()[0]) for each in input.readlines()]
input.seek(0)
right = [int(each.rstrip('\n').split()[1]) for each in input.readlines()]
left.sort()
right.sort()

total = 0
for i in range(len(left)):
    total += abs(left[i] - right[i])
print("part 1:", total)

similarity_score = 0
for each in left:
    similarity_score += each * right.count(each)
print("part 2:", similarity_score)