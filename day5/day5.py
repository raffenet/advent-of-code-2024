import sys

if len(sys.argv) >= 2 and sys.argv[1] == '-s':
    filename = 'day5/sample.txt'
else:
    filename = 'day5/input.txt'

input = open(filename, 'r')
foo = [each.rstrip() for each in input.readlines()]
ordering_rules = [each.split('|') for each in foo[0:21]]
updates = [each.split(',') for each in foo[22:]]
