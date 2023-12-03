from collections import defaultdict
from utils import get_adj, get_data

data = get_data('day03/in.txt')

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
                for x,y in get_adj(data, i, j):
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
