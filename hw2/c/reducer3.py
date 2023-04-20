#!/usr/bin/env python
"""mapper.py"""
import sys
import os 
thres = 0.005
total_basket_number = 4984636
current_pair =None
current_count=0
count=0
for line in sys.stdin:
    line = line.strip()
    pair,count = line.split('\t')
    count =int(count)
    pair=pair.strip()
    if current_pair == pair:
        current_count += count
    else:
        if current_pair:
            cur_p = (float(current_count)/float(total_basket_number))
            if cur_p >= thres:
            # write result to STDOUT
                print '%s\t%s' % (current_pair, current_count)
        current_count = count
        current_pair = pair
  
if current_pair == pair:
    cur_p = (float(current_count)/float(total_basket_number))
    if cur_p >= thres:
        print '%s\t%s' % (current_pair, current_count)
    
    
