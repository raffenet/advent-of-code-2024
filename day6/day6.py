import sys

if len(sys.argv) >= 2 and sys.argv[1] == '-s':
    filename = 'day6/sample.txt'
else:
    filename = 'day6/input.txt'

input = open(filename, 'r')
map = [each.strip() for each in input.readlines()]


