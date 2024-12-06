import sys

if len(sys.argv) >= 2 and sys.argv[1] == '-s':
    filename = 'day5/sample.txt'
else:
    filename = 'day5/input.txt'

input = open(filename, 'r')
foo = [each.rstrip() for each in input.readlines()]
ordering_rules = {}
for each in foo[0:foo.index('')]:
    k,v = tuple(map(int, each.split('|')))
    if k in ordering_rules.keys():
        ordering_rules[k].append(v)
    else:
        ordering_rules[k] = [v]
updates = [map(int, each.split(',')) for each in foo[foo.index('')+1:]]

def correct(update):
    tmp = list(update)
    for page in tmp:
        if page in ordering_rules:
            for rule in ordering_rules[page]:
                if rule in tmp[:tmp.index(page)]:
                    return 0
    return tmp[int(len(tmp)/2)]
print("part 1:", sum(map(correct, updates)))
