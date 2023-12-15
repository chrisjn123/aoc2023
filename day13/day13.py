patterns = [a.split() for a in open('in.txt').read().split('\n\n')]

pattern_sum = {i: 0 for i in range(len(patterns))}

def get_fold(d) -> int:
    for i in range(len(d)-1):
        if d[i] == d[i+1]:
            a, b = d[:i][::-1], d[i+2:]
            m = min(len(a), len(b))
            a,b = a[:m], b[:m]
            if a==b:
                return i+1
    return 0

def transpose(d) -> list[list]:
    return [''.join(f) for f in map(list, zip(*d))]

def find_smudged(d) -> int:
    for i in range(1, len(d)):
        diff = 0
        for n, row in enumerate(d):
            if n == i and diff == 1:
                return i
            mirrored = i * 2 - 1 - n
            if mirrored < len(d):
                diff += sum(1 for char1, char2 in zip(row, d[mirrored]) if char1 != char2)
                if diff > 1:
                    break

for num, patt in enumerate(patterns):
    val = get_fold(transpose(patt))
    if val:
        pattern_sum[num] += val
        continue
    val = 100*get_fold(patt)
    pattern_sum[num] += val

print(sum(pattern_sum.values()))

for num, patt in enumerate(patterns):
    pattern_sum[num] = 0
    val = find_smudged(transpose(patt))
    if val:
        pattern_sum[num] += val
        continue
    val = 100*find_smudged(patt)
    pattern_sum[num] += val

print(sum(pattern_sum.values()))

print()