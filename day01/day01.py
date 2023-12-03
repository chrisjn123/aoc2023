from itertools import product, combinations
from collections import defaultdict, Counter
from re import findall

def main() -> None:
    with open('in.txt') as fh:
        data = [line.strip() for line in fh.readlines()]

    s = []
    
    for line in data:
        a = line
        a = a.replace('one', 'o1e')
        a = a.replace('two','t2o')
        a = a.replace('three', 't3e')
        a = a.replace('four', 'f4r')
        a = a.replace('five', 'f5e')
        a = a.replace('six', 's6x')
        a = a.replace('seven', 's7n')
        a = a.replace('eight', 'e8t')
        a = a.replace('nine', 'n9e')

        nums = findall(r'\d', a)
        nums = [nums[0], nums[-1]]
        s.append(int(''.join(nums)))

    print(sum(s))


if __name__ == '__main__':
    main()