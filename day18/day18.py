from utils import get_data
import numpy as np
from cv2 import floodFill
from collections import defaultdict
from sys import maxsize

from copy import copy

data = get_data('test.txt')
data = [tuple(line.split()) for line in data]

locations = set()
curr = (0,0)
locations.add(curr)
for line in data:
    x,y = curr
    _, _, h = line
    amt = int(h.replace('#','').replace('(','').replace(')','')[:5], 16) // 10
    dir = int(h.replace('#','').replace('(','').replace(')','')[-1])
    if dir == 3:
        dir = 'U'
    elif dir == 2:
        dir = 'L'
    elif dir == 1:
        dir = 'D'
    else:
        dir = 'R'

    for i in range(1, amt+1):
        if dir in ('R', 'D'):
            if dir == 'R':
                y+=1
            else:
                x+=1
        else:
            if dir == 'L':
                y-=1
            else:
                x-=1
        curr = (x,y)
        locations.add(curr)
print('Locations obtained')
mx = min([c[0] for c in locations])
my = min([c[1] for c in locations])

locations_old = copy(locations)
locations.clear()
ii = -maxsize
jj = -maxsize
for loc in locations_old:
    x,y = loc
    x -= mx
    y -= my
    ii = max(ii, x)
    jj = max(jj, y)
    locations.add((x,y))
del locations_old
print('Locations normalized')
ii += 1
jj +=1
map_ = {i: ['.']*(jj-1) for i  in range(ii)}
'''for i in range(ii):
    for j in range(jj):
        if (i, j) in locations:
            map_[i].append('#')
        else:
            map_[i].append('.')'''
for x,y in locations:
    map_[i][j] = '#'
print('Map Built')
lMap = []
for l in map_.values():
    lMap.append(l)

blank = [['.']* (len(lMap[0])+2)]
for i, line in enumerate(lMap):
    lMap[i] = ['.'] + line + ['.']

lMap = blank + lMap + blank
print('Map buffered')
matrix = np.asarray(lMap)
numeric = np.where(matrix!='.', 255, 0).astype(np.uint8)
mask = np.zeros(np.asarray(numeric.shape)+2, dtype=np.uint8)
start_pt = (2,2)
if matrix[start_pt]:
    floodFill(numeric, mask, start_pt, 255, flags=4)
mask = mask[1:-1, 1:-1]
matrix[mask==1] = ' '
matrix = matrix.tolist()
for line in matrix:
    print(''.join(line))
vals = [1 for line in matrix for ch in line if ch in ('.', '#')]

print(len(vals))