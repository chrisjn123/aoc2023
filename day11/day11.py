from utils import *
from collections import defaultdict
from re import findall
from itertools import combinations
import numpy as np

def print_galaxy(d):
    for line in d:
        for c in line:
            print(c, end='')
        print()

data = get_data('test.txt')
for i, line in enumerate(data):
    data[i] = list(line)

idx_row = [i for i, line in enumerate(data) if all(j == '.' for j in line)]

idx_col = []
for j in range(0, len(data[0])):
    v = []
    for i in range(0, len(data)):
        v.append(data[i][j])
    if all(k=='.' for k in v):
        idx_col.append(j)

gal = defaultdict(tuple)
key = 1
for i, line in enumerate(data):
    for j, c in enumerate(line):
        if c == '#':
            data[i][j] = key
            gal[key] = (i,j)
            key += 1

pairs = set([i for i in combinations(gal.keys(),2)])

for g, coord in gal.items():
    i,j = coord
    for ii, x in enumerate(idx_row):
        for jj, y in enumerate(idx_col):
            if i < x:
                if j < y:
                    continue
                else:
                    gal[g] = (i, (10*(jj+1)) + j)
            elif i > x:
                if j < y:
                    gal[g] = (i + (10*(ii+1)), j)
                else:
                    gal[g] = (i + (10*(+1)), j + (10*(jj+1)))

s = 0
for f, t in pairs:
    f_c, t_c = gal[f], gal[t]
    d1 = abs(f_c[0] - t_c[0])
    d2 = abs(f_c[1] - t_c[1])
    #print(f'{f}->{t}: {d1+d2}')
    s += (d1+d2)
print(s)
print(len(pairs))