#!/usr/bin/env python
"""reducer3.py"""
from operator import itemgetter
import sys
current_paired_follower = None
paired_follower =None
current_key_follower = None
key_follower = None
follower_dict = {}
current_count = 0
common_followees = []
# input comes from STDIN
for line in sys.stdin:
    line = line.strip()
    key_follower, paired_follower, common_followee , count= line.split('\t')
    try:
        count = int(count)
    except ValueError:
        continue
    if current_key_follower == key_follower:
        common_followees,current_count = follower_dict.get(paired_follower,([],0))
        current_count += count
        common_followees.append(common_followee)
        follower_dict[paired_follower] = (common_followees,current_count)
    else:
        if current_key_follower:
            for k,v in follower_dict.items():
                print('%s\t%s\t{' % (current_key_follower, k)+','.join(v[0])\
            +'}, %s'%(v[1]))
                print('%s\t%s\t{' % (k, current_key_follower)+','.join(v[0])\
            +'}, %s'%(v[1]))
        current_count = count
        current_key_follower = key_follower
        current_paired_follower = paired_follower
        follower_dict = {}
        common_followees=[]
        common_followees.append(common_followee)
        follower_dict[current_paired_follower] = (common_followees,current_count)
        
for k,v in follower_dict.items():
    print('%s\t%s\t{' % (current_key_follower, k)+','.join(v[0])\
            +'}, %s'%(v[1]))
    print('%s\t%s\t{' % (k, current_key_follower)+','.join(v[0])\
            +'}, %s'%(v[1]))

