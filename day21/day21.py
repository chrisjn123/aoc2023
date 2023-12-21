from utils import get_data
from heapq import heappush, heappop
from itertools import product

points = set()
filename = 'in.txt'
TARGET = 6 if filename == 'test.txt' else 64

data = [list(line) for line in get_data(filename)]
for i, line in enumerate(data):
    for j, ch in enumerate(line):
        if ch == 'S':
            start = (i,j)
print(f'Starting point is: {start}')

def search(state: tuple[int]):
    global TARGET, data
    x, y = state
    seen = set()
    q = []
    heappush(q, (0,state))

    while len(q):
        print(f'Length of queue: {len(q)}')
        score, (x,y) = heappop(q)
        if x < 0 or x >= len(data) or y < 0 or y >= len(data) or score > TARGET or data[x][y] == '#':
            continue

        if score == TARGET and data[x][y] == '.':
            points.add((x,y))
            continue
        if (x,y) in seen:
            continue
        if data[x-1][y] == '.':
            heappush(q, (score+1, (x-1,y)))
        if data[x+1][y] == '.':
            heappush(q, (score+1, (x+1,y)))
        if data[x][y-1] == '.':
            heappush(q, (score+1, (x,y-1)))
        if data[x][y+1] == '.':
            heappush(q, (score+1, (x,y+1)))

search(start)
print(len(points)+1)