from re import findall
from itertools import product

data = open('test.txt').read().split('\n\n')
rules_raw = data[0].split()
in_vals = data[1].split()
rating = []
rules = {line.split('{')[0]: line.split('{')[1].replace('}','').split(',') for line in rules_raw}

def check(x,m,a,s):
    global rating, rules
    rule_key = 'in'
    done = False
    while True:
        if rule_key not in rules.keys():
            rating.append(rule_key)
            done = True
            break
        rule = rules[rule_key]
        for r in rule:
            if r[0] in 'xmas' and not r[1].isalpha():
                if eval(r.split(':')[0]):
                    rule_key = r.split(':')[-1]
                    break
            else:
                if r in rules.keys():
                    rule_key = r
                    break
                else:
                    rating.append(r)
                    done = True
                    break
        if done:
            break
from concurrent.futures import ThreadPoolExecutor
with ThreadPoolExecutor(max_workers=4) as pool:
    for x,m,a,s in product(range(1,4001), range(1,4001),
                           range(1,4001),range(1,4001)):
        pool.submit(check(x,m,a,s))

print(len([r for r in rating if r == 'A']))