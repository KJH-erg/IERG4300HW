#!/usr/bin/env python
import sys
import os 
import itertools
hash_fuct = {}
with open ('freq_items' ,'r') as f:
    data = f.read()
for i in data.split('\n')[0:-1]:
    i = i.split('\t')[0]
    hash_fuct[i] = 1
total_basket_number = 0
hash_table ={}
single_count={}
for basket in sys.stdin:
    basket = basket.strip()
    items = basket.split()
    pairs = itertools.combinations(items,2)
    for i in pairs:
        i = sorted(i)
        hash_key =hash(i[0]+i[1])%100000
        if "%"+str(hash_key) in hash_fuct:
            if i[0] in hash_fuct and i[1] in hash_fuct:
                print(i[0]+i[1]+'\t1')
        else:
            pass