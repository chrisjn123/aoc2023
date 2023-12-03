''' Utilities for Advent of Code '''

from itertools import product
from re import findall

def get_adj(data: list, x: int, y: int) -> list:
    adj = []
    for i,j in product((-1, 0, 1), (-1, 0, 1)):
        if i == 0 and j == 0:
            continue
        xi = x + i; yj = y + j
        try:
            data[xi][yj]
        except IndexError:
            continue
        else:
            if xi >= 0 and yj >= 0:
                adj.append((xi,yj))
    return adj

def get_data(file_name: str) -> list:
    with open(file_name) as fh:
        data = [line.strip() for line in fh.readlines()]
    if len(data) == 1:
        data = data[0]
    return data 

def scan_int(file_name: str, mode: bool) -> list:
    d = get_data(file_name)
    if mode:
        pattern = r'\d'
    else:
        pattern = r'\d+'
    
    res = [list(map(int, findall(pattern, a))) for a in d]

    return res


if __name__ == '__main__':
    assert(len(get_adj([[0]*10]*10, 1, 1)) == 8)
    assert(len(get_adj([[0]*10]*10, 0, 0)) == 3)

    assert(len(get_data('../tests/example.txt')) == 3)

    assert(scan_int('../tests/example.txt', False)[0][-1] == 13)
    assert(len(scan_int('../tests/example.txt', False)[0]) == 3)

    assert(scan_int('../tests/example.txt', True)[0][-1] == 3)
    assert(len(scan_int('../tests/example.txt', True)[0]) == 4)
