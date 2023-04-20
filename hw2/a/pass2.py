#!/usr/bin/env python
import sys
import os 
import itertools
# list for the frequent item
frequent_items = {}
# save frequent item into memmory in form of list 
with open("pass1.txt") as f:
    data = f.read()
# omit the last empty line
for i in data.split('\n')[0:-1]:
    frequent_items[i] = 1
# hash table for item pair with count
pair_count = {}
# counting the total number of baskets
total_basket_number = 0
# given threshold
thres = 0.01
#read original data 
with open ('yelp_review','r') as f:
    data = f.read()
data = data.split('\n')[0:-1]
# loop for each basket
for basket in data:
    basket = basket.strip()
# split basket into items
    items = basket.split()
# create all possible pairs with items
    freq_pairs = itertools.combinations(items,2)
# for each frequent pair
    for i in freq_pairs:
# sort first to avoid the situation (A,B) and (B,A) are counted differently
        i = tuple(sorted(i))
        if i[0] in frequent_items and i[1] in frequent_items:
# if each item in pair are both frequent(exist in frequent_items dictionary)
# increase count by 1
            cnt = pair_count.get(i,0)
            cnt=cnt+1
#save the increased count for the pair
            pair_count[i] = cnt
    total_basket_number = total_basket_number+1
# save the result part
with open('pass2.txt') as f:
# for each hashed pair
    for pair,count in pair_count.items():
# if count is more than threshold
        if float(int(count)/total_basket_number) >= thres:
#save the pair with count
            f.write(str(pair)+'\t'+str(count))