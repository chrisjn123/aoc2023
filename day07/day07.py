from collections import defaultdict, Counter
from itertools import product
from functools import cmp_to_key
from re import findall

from utils import get_data

data = get_data('in.txt')

order = {
    'A': 14, 'K': 13,
    'Q': 12, 'J': 1,
    'T': 10, '9': 9,
    '8': 8, '7': 7,
    '6': 6, '5': 5,
    '4': 4, '3': 3,
    '2': 2
}

def is_five_of(hand):
    cards = Counter(hand)
    for key, val in cards.items():
        if val == 5:
            return True
    return False

def is_four_of(hand):
    cards = Counter(hand)
    high = 0
    for key, val in cards.items():
        if val == 4:
            high = key
            return True
    return  False

def is_full_house(hand):
    cards = Counter(hand)
    if len(cards.keys()) == 2:
        high = [k for k, v in cards.items() if v == 3][0]
        return True
    return False

def is_three_of(hand):
    cards = Counter(hand)
    for key, val in cards.items():
        if val == 3:
            return True
    return False

def is_two_pair(hand):
    cards = Counter(hand)
    pairs = [k for k, v in cards.items() if v==2]
    if len(pairs) == 2:
        return True
    return False

def is_one_pair(hand):
    cards = Counter(hand)
    pairs = [k for k, v in cards.items() if v==2]
    if len(pairs) == 1:
        return True
    return False

def high_card(hand):
    global order
    h = max([order[l] for l in hand])
    return h

def get_best(hand: str):
    bests = defaultdict(list)
    for c in order:
        if c == 'J':
            continue
        nh = hand.replace('J', c)
        if is_five_of(nh):
            bests['5'].append(nh)
        elif is_four_of(nh):
            bests['4'].append(nh)
        elif is_full_house(nh):
            bests['f'].append(nh)
        elif is_three_of(nh):
            bests['3'].append(nh)
        elif is_two_pair(nh):
            bests['2'].append(nh)
        elif is_one_pair(nh):
            bests['1'].append(nh)
        else:
            bests['h'].append(nh)
        
        tmp = []
        for h in bests['5']:
            tmp.append(h)
        for h in bests['4']:
            tmp.append(h)
        for h in bests['f']:
            tmp.append(h)
        for h in bests['3']:
            tmp.append(h)
        for h in bests['2']:
            tmp.append(h)
        for h in bests['1']:
            tmp.append(h)
        for h in bests['h']:
            tmp.append(h)

    return tmp[0]

scores = defaultdict(int)
for line in data:
    card, value = line.split()
    value = int(value)
    #card = get_best(card) if 'J' in card else card
    scores[card] = value

card_orders = {
    'five': [],
    'four': [],
    'full': [],
    'three': [],
    'two': [],
    'one': [],
    'high': []
}

def compare(card_1, card_2):
    global order
    for x,y in zip(card_1[0], card_2[0]):
        xn = order[x]
        yn = order[y]

        if x == y:
            continue
        if xn > yn:
            return 1
        elif xn < yn:
            return -1

j_to_best = defaultdict(str)
for card in scores:
    if 'J' in card:
        j_to_best[card] = get_best(card)

for hand in scores:
    card = hand if hand not in j_to_best.keys() else j_to_best[hand]

    if is_five_of(card):
        card_orders['five'].append(card)
    elif is_four_of(card):
        card_orders['four'].append(card)
    elif is_full_house(card):
        card_orders['full'].append(card)
    elif is_three_of(card):
        card_orders['three'].append(card)
    elif is_two_pair(card):
        card_orders['two'].append(card)
    elif is_one_pair(card):
        card_orders['one'].append(card)
    else:
        card_orders['high'].append(card)

def num(card):
    ret = [order[c] for c in card]
    if ret == None or ret == []:
        print()
    return ret

high = sorted([(card, high_card(card)) for card in card_orders['high']], key=cmp_to_key(compare))
ones = sorted([(card, num(card)) for card in card_orders['one']], key=cmp_to_key(compare))
twos = sorted([(card, num(card)) for card in card_orders['two']], key=cmp_to_key(compare))
three = sorted([(card, num(card)) for card in card_orders['three']], key=cmp_to_key(compare))
full = sorted([(card, num(card)) for card in card_orders['full']], key=cmp_to_key(compare))
four = sorted([(card, num(card)) for card in card_orders['four']], key=cmp_to_key(compare))
five = sorted([(card, num(card)) for card in card_orders['five']], key=cmp_to_key(compare))

ranks = []
for a in high:
    ranks.append(a[0])
for a in ones:
    ranks.append(a[0])
for a in twos:
    ranks.append(a[0])
for a in three:
    ranks.append(a[0])
for a in full:
    ranks.append(a[0])
for a in four:
    ranks.append(a[0])
for a in five:
    ranks.append(a[0])

s = 0
for i, hand in enumerate(ranks):
    r = i + 1
    if hand in j_to_best.values():
        for f, t in j_to_best.items():
            if t == hand:
                card = f
                break
    else:
        card = hand
    bid = scores[card]
    print(f'{card}: rank: {r} with bid {bid}')
    s += (r * bid)

print(s)