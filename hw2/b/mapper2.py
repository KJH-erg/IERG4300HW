#!/usr/bin/env python
import sys
import os 
import itertools
# dictionary saving frequent item
frequent_items = {}
with open("freq_items",'r') as f:
    data = f.read()
# save the frequent items
for i in data.split('\n')[0:-1]:
    frequent_items[i.strip()] = 1

# for each basket
for basket in sys.stdin:
    basket = basket.strip()
    items = basket.split()
# generate all pairs of items
    freq_pairs = itertools.combinations(items,2)
# for each pair
    for i in freq_pairs:
# if each item is frequent (in frequent items dictionary)
        if i[0] in frequent_items and i[1] in frequent_items:
# sort the items within pair then print with count
            i = tuple(sorted(i))
            print((i[0]+":"+i[1])+'\t'+"1")