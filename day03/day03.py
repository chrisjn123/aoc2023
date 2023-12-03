from collections import *
from itertools import *
from re import findall
import sys

data = [line.strip() for line in open('in.txt').readlines()]

if len(data) == 1:
    data = data[0]
elif len(data) == 0:
    print('No data gathered.')
    sys.exit(0)

def get_adj(i, j) -> list:
    global data
    tmp = [
        (i-1, j-1), (i-1, j), (i-1, j+1),
        (i, j-1),             (i, j+1),
        (i+1, j-1), (i+1, j), (i+1, j+1)
    ]
    adj = []
    for a, b in tmp:
        if (a >=0 and b >= 0) and (a < len(data) and b < len(data[0])):
            adj.append((a,b))
    return adj

res = 0
part_nums = []
gears = defaultdict(list)
for i, row in enumerate(data):
    continuation = False
    val = 0
    for j, ch in enumerate(row + '.'):
        if not ch.isnumeric():
            if continuation:
                res += val
                part_nums.append(val)
                if data[x][y] == '*':
                    gears[(x,y)].append(val)
            continuation = False
            val = 0
        else:
            val = (val*10) + int(ch)
            if not continuation:
                for x,y in get_adj(i, j):
                    if data[x][y] not in ['.','1','2','3','4','5','6','7','8','9','0']:
                        continuation = True
                        break

# checks the list for each gear and makes sure that its only 2 adj nums, 
values = []
for l in gears.values():
    if len(l) == 2:
        values.append(l[0] * l[1])

print(res)
print(sum(values))