#!/usr/bin/env python
"""reducer2.py"""
import sys
import os 
thres = 0.01
current_pair=None
current_count=0
total_basket_number = 10
# for each line
for line in sys.stdin:
    line = line.strip()
    pair,count=line.split('\t')
    count =int(count)
# If the idential pair is received add the count
    if current_pair == pair:
        current_count += count
# If new pair is detected
    else:
        if current_pair:
            cur_p = (float(current_count)/float(total_basket_number))
            if cur_p >= thres:
                print (current_pair+'\t'+str(current_count))

#Assign new pair for the further counting
    current_count = count
    current_pair = pair
#to ensure last line is printed depending on the condition
if current_pair == pair:
    cur_p = (float(current_count)/float(total_basket_number))
    if cur_p >= thres:
        print (current_pair+'\t'+str(current_count))