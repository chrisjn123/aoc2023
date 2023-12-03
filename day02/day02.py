from collections import *
from itertools import *
from re import findall

data = [line.strip() for line in open('in.txt').readlines()]

if len(data) == 1:
    data = data[0]

games = defaultdict(list)
for game in data:
    id, res = game.split(':')
    id = findall(r'\d+', id)[0]
    for r in res.split(';'):
        colors = defaultdict(int)
        for cv in r.split(','):
            val, color = cv.split()
            val = int(val)
            colors[color] = val
        games[id].append(colors)

powers = defaultdict(int)
for game, runs in games.items():
    g_min, r_min, b_min = None, None, None
    for run in runs:
        if g_min is None and 'green' in run.keys():
            g_min = run['green']
        if r_min is None and 'red' in run.keys():
            r_min = run['red']
        if b_min is None and 'blue' in run.keys():
            b_min = run['blue']

        if 'green' in run.keys():
            g_min = run['green'] if run['green'] > g_min else g_min    
        if 'red' in run.keys():
            r_min = run['red'] if run['red'] > r_min else r_min    
        if 'blue' in run.keys():
            b_min = run['blue'] if run['blue'] > b_min else b_min

    power = g_min * r_min * b_min
    powers[game] = power

print(sum(powers.values()))