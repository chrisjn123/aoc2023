from utils import get_data

data = [list(map(int, a.split())) for a in get_data('in.txt')]

def diff(vals):
    return [y -x for x,y in zip(vals, vals[1:])]

def get_next(values: list) -> int:
    return values[-1] + get_next(diff(values)) if not all(t == 0 for t in values) else 0

#p1
print(sum([get_next(a) for a in data]))

#p2
print(sum([get_next(a[::-1]) for a in data]))