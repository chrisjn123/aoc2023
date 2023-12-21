from utils import get_data
from heapq import heappush, heappop
from itertools import product

points = set()
TARGET = 6

def manhattan(x1: int, y1: int,
              x2: int, y2: int) -> int:
    global TARGET
    ret = abs(x1-x2) + abs(y1-y2)
    if ret == TARGET: print(f'({x1}, {y1}): {ret}')
    return ret

data = [list(line) for line in get_data('test.txt')]
for i, line in enumerate(data):
    for j, ch in enumerate(line):
        if ch == 'S':
            start = (i,j)
print(f'Starting point is: {start}')

def search(state: tuple[int]):
    global TARGET, data
    x,y = state
    seen = set()
    q = []
    heappush(q, (0,state))

    while len(q):
        score, (x,y) = heappop(q)
        if not (0<=x<len(data)<0 or 0<=y<len(data[0])):
            return
        if (x,y) in seen or score > TARGET or data[x][y] == '#':
            continue
        seen.add((x,y))

        if score == TARGET and data[x][y] == '.':
            points.add((x,y))
            continue
        
        heappush(q, (score+1, (x-1,y)))
        heappush(q, (score+1, (x+1,y)))
        heappush(q, (score+1, (x,y-1)))
        heappush(q, (score+1, (x,y+1)))

search(start)
print(len(points))