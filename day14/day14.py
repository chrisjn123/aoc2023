from utils import get_data

data = get_data('in.txt')

T = list(map(list, zip(*data)))

s = 0
length = len(T)
for i, row in enumerate(T):
    row = ''.join(row).split('#')
    for j, t in enumerate(row):
        row[j] = ''.join(sorted(t, reverse=True))

    row = '#'.join(row)
    T[i] = row
    for v, ch in enumerate(row):
        if ch == 'O':
            s += (length -v)
print(s)