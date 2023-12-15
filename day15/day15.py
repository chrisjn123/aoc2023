from utils import get_data
from functools import lru_cache
from time import perf_counter
start = perf_counter()

data = get_data('in.txt')
data = data.split(',')

@lru_cache
def get_hash(curr_str: str):
    curr_value = 0
    for ch in curr_str:
        tmp = ord(ch)
        curr_value += tmp
        curr_value *= 17
        curr_value %= 256
    return curr_value

s = 0
for h in data:
    s += get_hash(h)
print(s)

boxes = {i:[] for i in range(256)}

stack_idx = 0
for ins in data:
    
    if '-' in ins:
        lbl = ins.split('-')[0]
        hash_val = get_hash(lbl)
        for label in boxes[hash_val]:
            if lbl in label:
                boxes[hash_val].remove(label)
                break
    
    elif '=' in ins:
        lbl = ins.split('=')[0]
        hash_val = get_hash(lbl)
        
        cont = False
        for label in boxes[hash_val]:
            if lbl in label:                
                idx = boxes[hash_val].index(label)
                boxes[hash_val][idx] = ins
                cont = True
                break
        if cont:
            continue
        boxes[hash_val].append(ins)
s = 0
for box, item in boxes.items():
    for i, it in enumerate(item):
        fl = int(it.split('=')[-1])
        v = (box+1) * (i+1) * fl
        s += v
print(s)
print(f"{perf_counter() - start}")