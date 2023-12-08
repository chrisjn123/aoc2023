from collections import  defaultdict
from itertools import product, cycle
from utils import *
from math import lcm
from time import perf_counter
from sys import setrecursionlimit
setrecursionlimit(10_000_000)

time_1 = perf_counter()

data = get_data('in.txt')

ins = cycle(data[0])

_map = defaultdict(tuple)
network = data[2:]
for line in network:
    key = line.split('=')[0].strip()
    left, right = line.split('=')[1].replace('(', '').replace(')', '').split(',')

    _map[key] = (left.strip(), right.strip())

count = 0
def go(point):
    global count, ins

    if point[-1] == 'Z':
        return
    move = 0 if next(ins) == 'L' else 1
    count += 1
    go(_map[point][move])

starts = [node for node in _map if node.endswith('A')]
curr = starts

ins_backup = ins

def check_z(arr):
    ret = [a[-1] == 'Z' for a in arr]
    return ret

counts = defaultdict(int)

for start in starts:
    count = 0
    go(start)
    counts[start] = count

print(lcm(*list(counts.values())))
print(perf_counter() - time_1)