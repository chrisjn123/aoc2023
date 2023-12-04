from collections import defaultdict
from concurrent.futures import ThreadPoolExecutor
from utils import get_adj, get_data
from re import findall
from itertools import product

data = get_data('test.txt')

cards = defaultdict(tuple)
for line in data:
    card_no = int(line.split(':')[0].replace('Card ', ''))
    winning = line.split(':')[-1].split('|')[0]
    my_num = line.split(':')[-1].split('|')[-1]

    winning = [int(a) for a in findall(r'\d+', winning)]
    my_num = [int(a) for a in findall(r'\d+', my_num)]
    
    cards[card_no] = (winning, my_num)

card_cal = defaultdict(int)
all_cards = defaultdict(list)
order_card = []
for card, nums in cards.items():
    order_card.append(card)
    w, n = nums
    count = 0
    matches = 0
    for i,j in product(w,n):
        if i == j:
            count = count *2 if count != 0 else 1
            matches += 1
    
    card_cal[card] = count
    if matches:
        for i in range(card+1, card+1+matches):
            all_cards[card].append(i)

    

print(sum(card_cal.values()))

alt = [card for card in card_cal.keys()]
for card in order_card:
    if card in all_cards.keys():
        for vals in all_cards.values():
            for i in vals:
                alt.append(i)
p2 = 0
counter = defaultdict(int)
for a in sorted(alt):
    counter[a] +=1
print(p2)