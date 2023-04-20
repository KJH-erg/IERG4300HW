#!/usr/bin/env python
"""reducer.py"""
from operator import itemgetter
import sys
current_followee =None
cur_follower_list = []
for line in sys.stdin:
    line = line.strip()
    followee, follower = line.split('\t')
    if current_followee == followee:
        cur_follower_list.append(follower)
    else:
        if current_followee:
            print '%s\t%s' % (current_followee, ','.join(cur_follower_list))
        cur_follower_list = []
        cur_follower_list.append(follower)
        current_followee =followee
print '%s\t%s' % (current_followee, ','.join(cur_follower_list))