#!/usr/bin/env python
import sys
import os 
import itertools
frequent_items = {}
with open("freq_items",'r') as f:
    data = f.read()
for i in data.split('\n')[0:-1]:
    frequent_items[i.strip()] = 1

pair_count={}

for basket in sys.stdin:
    basket = basket.strip()
    items = basket.split()
    filtered_freq_items = []
    for i in items:
        i = i.strip()
        try:
            if frequent_items[i] == 1:
                filtered_freq_items.append(i)
        except:
            pass
    freq_pairs = itertools.combinations(filtered_freq_items,2)
    for i in freq_pairs:
        i = tuple(sorted(i))
        cnt = pair_count.get(i,0)
        cnt = cnt+1
        pair_count[i] = cnt
for k,v in pair_count.items():
    print(k[0]+":"+k[1]+'\t'+str(v))
