import sys

if len(sys.argv) >= 2 and sys.argv[1] == '-s':
    filename = 'day6/sample.txt'
else:
    filename = 'day6/input.txt'

input = open(filename, 'r')
map = [each.strip() for each in input.readlines()]

left = "<"
right = ">"
up = "^"
down = "v"
guard = ""

def is_inbounds(x,y):
    return x >= 0 and x < len(map[0]) and y >= 0 and y < len(map)

def is_guard(char):
    return char == '^' or char == '>' or char == 'v' or char == '<'

def is_obstruction(x,y):
    return map[y][x] == '#'

def move(x, y, guard):
    newx = x
    newy = y
    if guard == up:
        if is_inbounds(x, y-1) and is_obstruction(x, y-1):
            guard = right
            return move(x, y, guard)
        newy = y-1
    elif guard == right:
        if is_inbounds(x+1, y) and is_obstruction(x+1, y):
            guard = down
            return move(x, y, guard)
        newx = x+1
    elif guard == down:
        if is_inbounds(x, y+1) and is_obstruction(x, y+1):
            guard = left
            return move(x, y, guard)
        newy = y+1
    elif guard == left:
        if is_inbounds(x-1, y) and is_obstruction(x-1, y):
            guard = up
            return move(x, y, guard)
        newx = x-1
    return newx, newy, guard

def find_guard(map):
    for y, row in enumerate(map):
        for x, char in enumerate(row):
            if is_guard(char):
                return x,y

pos = {}
x, y = find_guard(map)
guard = map[y][x]
pos[x,y] = 1
while is_inbounds(x, y):
    x, y, guard = move(x, y, guard)
    pos[x,y] = 1
print("part 1:", len(pos)-1)
