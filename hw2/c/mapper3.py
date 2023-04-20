#!/usr/bin/env python
import sys
import os 
import itertools
frequent_items = {}
pair_count ={}
    
with open("freq_pair",'r') as f:
    data = f.read()
for i in data.split('\n')[0:-1]:
    keys = i.strip()
    k1,k2 = keys.split('\t')
    k1 = k1.strip()
    k2 = k2.strip()
    frequent_items[k1] = True
    frequent_items[k2] = True

for basket in sys.stdin:
    basket = basket.strip()
    items = basket.split()
    filtered_freq_items = []
    for i in items:
        if i in  frequent_items:
            filtered_freq_items.append(i)
    triplets = itertools.combinations(filtered_freq_items,3)
    for i in triplets:
            # print(i)
        i = tuple(sorted(i))
        print(i[0]+':'+i[1]+":"+i[2]+'\t'+'1')
