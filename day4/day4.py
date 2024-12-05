import sys

if len(sys.argv) >= 2 and sys.argv[1] == '-s':
    filename = 'day4/sample.txt'
else:
    filename = 'day4/input.txt'

def left(x, y, wordsearch):
    if x >= 3 and wordsearch[y][x-1] == 'M' and wordsearch[y][x-2] == 'A' and wordsearch[y][x-3] == 'S':
        return 1
    return 0
    
def right(x, y, wordsearch):
    if x <= (len(wordsearch[0]) - 4) and wordsearch[y][x+1] == 'M' and wordsearch[y][x+2] == 'A' and wordsearch[y][x+3] == 'S':
        return 1
    return 0
    
def up(x, y, wordsearch):
    if y >= 3 and wordsearch[y-1][x] == 'M' and wordsearch[y-2][x] == 'A' and wordsearch[y-3][x] == 'S':
        return 1
    return 0
    
def down(x, y, wordsearch):
    if y <= (len(wordsearch) - 4) and wordsearch[y+1][x] == 'M' and wordsearch[y+2][x] == 'A' and wordsearch[y+3][x] == 'S':
        return 1
    return 0
    
def upleft(x, y, wordsearch):
    if x >= 3 and y >= 3 and wordsearch[y-1][x-1] == 'M' and wordsearch[y-2][x-2] == 'A' and wordsearch[y-3][x-3] == 'S':
        return 1
    return 0
    
def upright(x, y, wordsearch):
    if x <= (len(wordsearch[0]) - 4) and y >= 3 and wordsearch[y-1][x+1] == 'M' and wordsearch[y-2][x+2] == 'A' and wordsearch[y-3][x+3] == 'S':
        return 1
    return 0
    
def downleft(x, y, wordsearch):
    if x >= 3 and y <= (len(wordsearch) - 4) and wordsearch[y+1][x-1] == 'M' and wordsearch[y+2][x-2] == 'A' and wordsearch[y+3][x-3] == 'S':
        return 1
    return 0
    
def downright(x, y, wordsearch):
    if x <= (len(wordsearch[0]) - 4) and y <= (len(wordsearch) - 4) and wordsearch[y+1][x+1] == 'M' and wordsearch[y+2][x+2] == 'A' and wordsearch[y+3][x+3] == 'S':
        return 1
    return 0

input = open(filename, 'r')
num = 0
wordsearch = [each.rstrip() for each in input.readlines()]
for y, row in enumerate(wordsearch):
    for x, letter in enumerate(row):
        if letter == 'X':
            num += left(x, y, wordsearch) + right(x, y, wordsearch) \
                + up(x, y, wordsearch) + down(x, y, wordsearch) \
                + upleft(x, y, wordsearch) + upright(x, y, wordsearch) \
                + downleft(x, y, wordsearch) + downright(x, y, wordsearch)
print("part 1:", num)

def xmas(x, y, wordsearch):
    if x-1 < 0 or x+1 == len(wordsearch[0]) or y-1 < 0 or y+1 == len(wordsearch):
        return 0
    if wordsearch[y-1][x-1] == 'M' and wordsearch[y-1][x+1] == 'M' and wordsearch[y+1][x-1] == 'S' and wordsearch[y+1][x+1] == 'S':
        return 1
    if wordsearch[y-1][x-1] == 'S' and wordsearch[y-1][x+1] == 'S' and wordsearch[y+1][x-1] == 'M' and wordsearch[y+1][x+1] == 'M':
        return 1
    if wordsearch[y-1][x-1] == 'S' and wordsearch[y-1][x+1] == 'M' and wordsearch[y+1][x-1] == 'S' and wordsearch[y+1][x+1] == 'M':
        return 1
    if wordsearch[y-1][x-1] == 'M' and wordsearch[y-1][x+1] == 'S' and wordsearch[y+1][x-1] == 'M' and wordsearch[y+1][x+1] == 'S':
        return 1
    return 0

num = 0
for y, row in enumerate(wordsearch):
    for x, letter in enumerate(row):
        if letter == 'A':
            num += xmas(x, y, wordsearch)
print("part 2:", num)
