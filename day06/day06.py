from re import findall
from collections import defaultdict

from utils import get_data, get_adj

data = get_data('in.txt')

times = list(findall(r'\d+', data[0]))
distances = list(findall(r'\d+', data[1]))

times = [int(''.join(times))]
distances = [int(''.join(distances))]

races_way_to_win = defaultdict(int)

race_id = 1
for t, d in zip(times, distances):
    for hold_time in range(0, t):
        dist_gone = hold_time * (t - hold_time)
        if dist_gone > d:
            races_way_to_win[race_id] += 1
    
    race_id += 1

tmp = 1
for b in races_way_to_win.values():
    tmp *= b

print(tmp)