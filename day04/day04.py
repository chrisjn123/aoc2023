from collections import defaultdict
from concurrent.futures import ThreadPoolExecutor
from utils import get_adj, get_data
from re import findall
from itertools import product

data = get_data('in.txt')

cards = defaultdict(tuple)
for line in data:
    card_no = int(line.split(':')[0].replace('Card ', ''))
    winning = line.split(':')[-1].split('|')[0]
    my_num = line.split(':')[-1].split('|')[-1]

    winning = [int(a) for a in findall(r'\d+', winning)]
    my_num = [int(a) for a in findall(r'\d+', my_num)]
    
    cards[card_no] = (winning, my_num)

card_cal = defaultdict(int)
matches = defaultdict(int)

for card, nums in cards.items():
    w, n = nums
    count = 0
    for i,j in product(w,n):
        if i == j:
            count = count *2 if count != 0 else 1
            matches[card] += 1
    
    card_cal[card] = count

print(sum(card_cal.values()))

cards_count = defaultdict(int)
def get_next(i: int):
    global cards_count, card_cal, matches
    s = card_cal[i]
    cards_count[i] += 1
    if matches[i]:
        for nc in range(i+1, i+1+matches[i]):
            cards_count[nc] += 1
            s += get_next(nc)
    return s

si = 0

get_next(1)
missing = [card for card in cards if card not in cards_count]
print(sum(cards_count.values()) + len(missing))
print()