from collections import defaultdict
from more_itertools import distinct_permutations
from re import findall

from utils import get_data

data = get_data('in.txt')
springs = []
for line in data:
    sp = line.split()
    ints = list(map(int, findall(r'\d+', sp[1])))
    # ii = ints*5
    # a = (sp[0] + '?')*5
    springs.append((sp[0], ints))

count = defaultdict(int)
i = 0
for spring, order in springs:
    copy_spring = spring
    unknown = spring.count('?')
    pick = distinct_permutations('.'*unknown + '#'*unknown, unknown)
    try:
        while vals := next(pick):
            for v in vals:
                copy_spring = copy_spring.replace('?', v, 1)
            #print(copy_spring)
            # check copy_spring
            sp = copy_spring.split('.')
            lengths = [len(s) for s in sp if s]
            if len(lengths) != len(order):
                pass
            elif all(a==b for a,b in zip(lengths, order)):
                count[spring] += 1
            #reset spring
            copy_spring = spring
    except StopIteration:
        pass
        #print('_'*20)
    i += 1
    print(f'{i} of {len(data)}')
print(sum(count.values()))        

print()