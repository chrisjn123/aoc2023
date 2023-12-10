from collections import defaultdict

from utils import *

data = get_data('test.txt')

def deteremine_start(adj: list, x: int, y: int) -> str:
    pass

def directions(pipe: str, i: int, j: int) -> tuple:
    ''' Will return a tuple of (up, down, left, right) '''
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
            adj = get_adj(data, i, j)
            return deteremine_start(adj, i, j) or (0,0,0,0)
        case other:
            return (0,0,0,0)

for i, line in enumerate(data):
    data[i] = list(line)


_map = defaultdict(list)
for i, line in enumerate(data):
    for j, ch in enumerate(line):
        _map[i].append(directions(ch, i, j))

print()