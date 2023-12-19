from re import findall

data = open('in.txt').read().split('\n\n')
rules_raw = data[0].split()
in_vals = data[1].split()
rating = []
rules = {line.split('{')[0]: line.split('{')[1].replace('}','').split(',') for line in rules_raw}
for v in in_vals:
    x,m,a,s = list(map(int, findall(r'\d+', v)))
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
s = 0
for val, r in zip(in_vals, rating):
    if r == 'A':
        s += sum(list(map(int, findall(r'\d+', val))))
print(s)