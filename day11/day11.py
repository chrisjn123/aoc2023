from utils import *
from collections import defaultdict
from re import findall
from itertools import combinations

def print_galaxy(d):
    for line in d:
        for c in line:
            print(c, end='')
        print()

data = get_data('test.txt')
for i, line in enumerate(data):
    data[i] = list(line)

idx = [i for i, line in enumerate(data) if all(j == '.' for j in line)]
offset = 0
for i in idx:
    for _ in range(1_000_000):
        data.insert(i+offset, data[i+offset])
        offset += 1

idx = []
for j in range(0, len(data[0])):
    v = []
    for i in range(0, len(data)):
        v.append(data[i][j])
    if all(k=='.' for k in v):
        idx.append(j)

for i, line in enumerate(data):
    offset = 0
    for id in idx:
        for _ in range(1_000_000):
            data[i].insert(offset+id, '.')
            offset += 1

m = min([len(d) for d in data])
for i, line in enumerate(data):
    if all(k=='.' for k in line):
        data[i] = ['.']*m

gal = defaultdict(tuple)
key = 1
for i, line in enumerate(data):
    for j, c in enumerate(line):
        if c == '#':
            data[i][j] = key
            gal[key] = (i,j)
            key += 1

pairs = set([i for i in combinations(gal.keys(),2)])

s = 0
for f, t in pairs:
    f_c, t_c = gal[f], gal[t]
    d1 = abs(f_c[0] - t_c[0])
    d2 = abs(f_c[1] - t_c[1])
    #print(f'{f}->{t}: {d1+d2}')
    s += (d1+d2)
print(s)