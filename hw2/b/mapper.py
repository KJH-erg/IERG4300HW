#!/usr/bin/env python
import sys
import os 
hash_count={}
total_basket_number = 0
thres = 0.01
# number of mappers
p=7
# A-Priori algorithm part
for basket in sys.stdin:
    basket = basket.strip()
    items = basket.split()
    for item in items:
        tmp_cnt = hash_count.get(item,0)
        tmp_cnt = tmp_cnt+1
        hash_count[item] = tmp_cnt
    total_basket_number=total_basket_number+1
# Update ps
ps = thres*p
# if item count within a chunk
# is greater than ps print the result
for item,count in hash_count.items():
    if count>=ps:
        print((item)+'\t'+str(count))