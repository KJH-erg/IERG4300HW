#!/usr/bin/env python
import sys
import os 
"""mapper.py"""
hash_count={}
total_basket_number = 0
thres = 0.005
# number of chunks
p=7
for basket in sys.stdin:
    basket = basket.strip()
    items = basket.split()
    for item in items:
        tmp_cnt = hash_count.get(item,0)
        tmp_cnt = tmp_cnt+1
        hash_count[item] = tmp_cnt
    total_basket_number=total_basket_number+1
# update the threshold
thres = thres*p
for item,count in hash_count.items():
    cur_p = (float(count)/float(total_basket_number))
    if cur_p >= thres:
        print((item)+'\t'+str(count))