#!/usr/bin/env python
"""reducer3.py"""
from operator import itemgetter
import sys
current_pair1= None
current_pair2=None
current_count = 0
current_values = None
# input comes from STDIN
for line in sys.stdin:
    line = line.strip()
    pair1,pair2,values= line.split('\t')
    count = int(values.split('},')[1])
    if current_pair1 == pair1:
        if current_count < count:
            current_count = count
            current_values = values
            current_pair2 = pair2
        elif current_count == count and int(pair2) > int(current_pair2):
            current_count = count
            current_values = values
            current_pair2 = pair2
    else:
        if current_pair1:
            # write result to STDOUT
            print  (current_pair1+':'+current_pair2+' '+current_values)
        current_count = count
        current_pair1 = pair1
        current_values = values
        current_pair2 = pair2
if current_pair1 == pair1:
    print  (current_pair1+':'+current_pair2+' '+current_values)