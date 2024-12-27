import sys

if len(sys.argv) >= 2 and sys.argv[1] == '-s':
    filename = 'day6/sample.txt'
else:
    filename = 'day6/input.txt'

input = open(filename, 'r')
map = [list(each.strip()) for each in input.readlines()]

left = "<"
right = ">"
up = "^"
down = "v"

def is_inbounds(x,y):
    return x >= 0 and x < len(map[0]) and y >= 0 and y < len(map)

def is_guard(char):
    return char == '^' or char == '>' or char == 'v' or char == '<'

def is_obstruction(char):
    return char == '#'

def move(x, y, guard):
    newx = x
    newy = y
    if guard == up:
        if is_inbounds(x, y-1) and is_obstruction(map[y-1][x]):
            guard = right
            return move(x, y, guard)
        newy = y-1
    elif guard == right:
        if is_inbounds(x+1, y) and is_obstruction(map[y][x+1]):
            guard = down
            return move(x, y, guard)
        newx = x+1
    elif guard == down:
        if is_inbounds(x, y+1) and is_obstruction(map[y+1][x]):
            guard = left
            return move(x, y, guard)
        newy = y+1
    elif guard == left:
        if is_inbounds(x-1, y) and is_obstruction(map[y][x-1]):
            guard = up
            return move(x, y, guard)
        newx = x-1
    return newx, newy, guard

def find_guard(map):
    for y, row in enumerate(map):
        for x, char in enumerate(row):
            if is_guard(char):
                return x,y,map[y][x]

pos = {}
x, y, guard = find_guard(map)
pos[x,y] = 1
while is_inbounds(x, y):
    x, y, guard = move(x, y, guard)
    if (x,y) in pos.keys():
        pos[x,y] = pos[x,y] + 1
    else:
        pos[x,y] = 1
print("part 1:", len(pos)-1)

def is_loop(history):
    positions = len(map) * len(map[0])
    return sum(history.values()) > positions*2

import copy

orig_map = map
loops = 0
for j, row in enumerate(orig_map):
    for i, char in enumerate(row):
        if not is_obstruction(orig_map[j][i]) and not is_guard(orig_map[j][i]):
            map = copy.deepcopy(orig_map)
            map[j][i] = '#'
            pos = {}
            x, y, guard = find_guard(map)
            pos[x,y] = 1
            while is_inbounds(x, y):
                x, y, guard = move(x, y, guard)
                if (x,y) in pos.keys():
                    pos[x,y] = pos[x,y] + 1
                else:
                    pos[x,y] = 1
                if is_loop(pos):
                    loops = loops + 1
                    break

print("part 2:", loops)
