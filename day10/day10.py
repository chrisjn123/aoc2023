from collections import defaultdict

from utils import *
import numpy as np
import cv2

data = get_data('in.txt')
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
    '#': '\u2588',
    ' ': ' ',
    '.': '.'
}

for i in range(len(data)):
    for j in range(len(data[0])):
        if (i,j) not in path:
            data[i][j] = ' '
            _map[i][j] = (0,0,0,0)
        else:
            data[i][j] = letter_to_uni[data[i][j]]

# for i, line in enumerate(data):
#     data[i] = [' '] + line + [' ']
# blank = []
# for i in range(len(data[0])):
#     blank.append(' ')

#data.insert(0, blank)
#data.append(blank)

def print_loop(d) -> None:
    for line in d:
        for c in line:
            print(c, end='')
        print()

def flood(d):
    global start
    #print_loop(d)
    matrix = np.asarray(d)
    numeric = np.where(matrix!=' ', 255, 0).astype(np.uint8)
    mask = np.zeros(np.asarray(numeric.shape)+2, dtype=np.uint8)
    start_pt = (0,0)
    if matrix[start_pt]:
        cv2.floodFill(numeric, mask, start_pt, 255, flags=4)
    mask = mask[1:-1, 1:-1]
    matrix[mask==1] = '.'
    res = np.where(matrix==' ', 255, 0 ).astype(np.uint8).tolist()
    matrix = matrix.tolist()

    #print_loop(matrix)
    v = len([c for line in res for c in line if c == 255])
    return v

print(flood(data))

print_loop(data)
data_big = []
for i in range(4*len(data)):
    a = []
    for j in range(4*len(data[0])):
        a.append(' ')
    data_big.append(a)

pieces = {
    letter_to_uni['|']: [[' ', '#', ' '],
                         [' ', '#', ' '],
                         [' ', '#', ' '],],
    letter_to_uni['-']: [[' ',' ',' '],
                         ['#','#','#'],
                         [' ',' ',' ']],
    letter_to_uni['L']: [[' ','#',' '],
                         [' ','#','#'],
                         [' ',' ',' ']],
    letter_to_uni['7']: [[' ',' ',' '],
                         ['#','#',' '],
                         [' ','#',' ']],
    letter_to_uni['F']: [[' ',' ',' '],
                         [' ','#','#'],
                         [' ','#',' ']],
    letter_to_uni['J']: [[' ','#',' '],
                         ['#','#',' '],
                         [' ',' ',' ']],
    letter_to_uni['S']: [[' ',' ',' '],
                         ['#','#',' '],
                         [' ','#',' ']]
}


for coord in path:
    x,y = coord
    piece = data[x][y]
    x = (3*x) + 2
    y = (3*y) + 2
    for i, j in product(range(3), range(3)):
        if piece in pieces.keys():
            data_big[x+i][y+j] = letter_to_uni[pieces[piece][i][j]]
        else:
            print(f'Piece: {piece} Coord: {coord}')

print(flood(data_big) // 81)
print()