#!/usr/bin/env python
import sys
import os 
import itertools
pair_hash = {}
with open("filtered.txt") as f:
    data = f.read()
frequent_item = []
for i in data.split('\n')[0:-1]:
    frequent_item.append(i)
pair_count = {}

for line in sys.stdin:
    line = line.strip()
    items = line.split()
    filtered_freq_items = set(frequent_item) & set(items)
    freq_pairs = itertools.combinations(filtered_freq_items,2)
    for i in freq_pairs:
        i = tuple(sorted(i))
        cnt = pair_count.get(i,0)
        cnt=cnt+1
        pair_count[i] = cnt
for k,v in pair_count.items():
    print(str(k)+'\t'+str(v))
