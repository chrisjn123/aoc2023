data = [a.split() for a in open('in.txt').read().split('\n\n')]

def transform(D: list[list]) -> list[list]:
    T = list(map(list, zip(*D)))
    return [''.join(x) for x in T]

def get_fold(pattern: list[list]) -> int:
    for a, b in zip(pattern, pattern[1:]):
        if a==b:
            i = pattern.index(a)
            n = 1
            m = False
            while n+1+i < len(pattern) and i-n >= 0:
                if pattern[n+1+i] == pattern[i-n]:
                    n += 1
                    m = True
                else:
                    m = False
                    break
            return i+1 if m else 0
    return 0
s = 0
for patt in data:
    if a:=get_fold(patt):
        s += 100*a
    else:
        s += get_fold(transform(patt))
print(s)