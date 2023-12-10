from collections import defaultdict

from utils import *
import numpy as np

data = get_data('test.txt')
for i, line in enumerate(data):
    data[i] = list(line)

start = (0,0)
def directions(pipe: str, i: int, j: int) -> tuple:
    ''' Will return a tuple of (up, down, left, right) '''
    global start
    match(pipe):
        case '|':
            return (1,1,0,0)
        case '-':
            return (0,0,1,1)
        case 'L':
            return (1,0,0,1)
        case 'J':
            return (1,0,1,0)
        case '7':
            return (0,1,1,0)
        case 'F':
            return (0,1,0,1)
        case 'S':
            start = (i, j)
            return (0,1,0,0)
        case other:
            return (0,0,0,0)

_map = defaultdict(list)
for i, line in enumerate(data):
    for j, ch in enumerate(line):
        _map[i].append(directions(ch, i, j))

flag = True
r,c = start
count = 0
prev = np.array((0,0,0,0))

path = []

while data[r][c] != 'S' or flag:
    path.append((r,c))
    flag = False
    curr = np.array(_map[r][c])
    res = [i if i > 0 else 0 for i in curr - prev]
    up, down, left, right = res
    
    if up:
        r -= 1
    elif down:
        r += 1
    elif left:
        c -= 1
    elif right:
        c += 1

    prev = np.array((down, up, right, left))
    count += 1
print(count, count // 2)

letter_to_uni = {
    'J': '\u2518',
    '-': '\u2500',
    '|': '\u2502',
    '7': '\u2510',
    'F': '\u250C',
    'S': '\u2573',
    'L': '\u2514',
}

for i in range(len(data)):
    for j in range(len(data[0])):
        if (i,j) not in path:
            data[i][j] = ' '
            _map[i][j] = (0,0,0,0)
        else:
            data[i][j] = letter_to_uni[data[i][j]]

for i, line in enumerate(data):
    data[i] = [' '] + line + [' ']

def print_loop() -> None:
    global data
    for line in data:
        for c in line:
            print(c, end='')
        print()

def flood():
    global data