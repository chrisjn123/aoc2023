from utils import get_data
from re import findall

data = get_data('in.txt')
seeds, maps = list(map(int, findall(r'\d+', data.split('\n\n')[0]))), data.split('\n\n')[1:]

maps = {
    d.split('\n')[0]: d.split('\n')[1:]
    for d in maps
}

print('Starting searches')
locs = []
for seed in seeds:
    tmp = seed
    for m_data in maps.values():
        for vals in m_data:
            dst, src, length = map(int, findall(r'\d+', vals))
            if tmp in range(src, length+src):
                tmp = dst - src + tmp
                break
    locs.append(tmp)
print(min(locs))