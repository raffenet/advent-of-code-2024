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

incorrect = []
def correct(update):
    tmp = list(update)
    for page in tmp:
        if page in ordering_rules:
            for rule in ordering_rules[page]:
                if rule in tmp[:tmp.index(page)]:
                    incorrect.append(tmp)
                    return 0
    return tmp[int(len(tmp)/2)]
print("part 1:", sum(map(correct, updates)))

def cmp(a, b):
    if a in ordering_rules and b in ordering_rules[a]:
        return -1
    elif b in ordering_rules and a in ordering_rules[b]:
        return 1
    return 0

import functools
def fix(update):
    update.sort(key=functools.cmp_to_key(cmp))
    return update[int(len(update)/2)]

print("part 2:", sum(map(fix, incorrect)))
