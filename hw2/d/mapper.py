#!/usr/bin/env python
import sys
import os 
import itertools
hash_count={}
item_count={}
total_basket_number = 0
thres = 0.01
# number of mappers
p=7
# Update ps
ps = thres/p
# A-Priori algorithm part
for basket in sys.stdin:
    basket = basket.strip()
    items = basket.split()
# part to count the number of item and save in
# item_count dictionary
    for item in items:
        tmp_cnt = item_count.get(item,0)
        item_count[item] = tmp_cnt+1
# create all possible pairs
    pairs = itertools.combinations(items,2)
    for i in pairs:
# sort the pair
        i = sorted(i)
# create hash key
        hash_key =hash(i[0]+i[1])%100000
# part to count the number of hash key and save in
# hash_count dictionary
        tmp = hash_count.get(hash_key,0)
        hash_count[hash_key] = tmp+1
# count the total number of chunk
	total_basket_number=total_basket_number+1
# if item count within a chunk
# is greater than ps print the result to reducer
for item,count in item_count.items():
    if count>=ps:
        print((item)+'\t'+str(count))
# if hash key count within a chunk
# is greater than ps print the result to reducer
for hash,count in hash_count.items():
    if count>=ps:
        print("%"+str(hash)+'\t'+str(count))