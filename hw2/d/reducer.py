#!/usr/bin/env python
"""mapper.py"""
import sys
import os 
thres = 0.01
current_pair=None
current_count=0
total_basket_number = 4984636
for line in sys.stdin:
    line = line.strip()
    pair,count=line.split('\t')
    count =int(count)
    if current_pair == pair:
        current_count += count
    else:
        if current_pair:
            cur_p = (float(current_count)/float(total_basket_number))
            if cur_p >= thres:
                print (current_pair)
        current_count = count
        current_pair = pair

if current_pair == pair:
    cur_p = (float(current_count)/float(total_basket_number))
    if cur_p >= thres:
        print (current_pair)