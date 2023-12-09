from utils import get_data

data = [list(map(int, a.split())) for a in get_data('in.txt')]

def get_next(values: list) -> int:
    return values[-1] + get_next([y -x for x,y in zip(values, values[1:])]) if not all(t == 0 for t in values) else 0

print(sum([get_next(a) for a in data]))
print(sum([get_next(a[::-1]) for a in data]))