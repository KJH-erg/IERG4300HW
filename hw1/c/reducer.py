#!/usr/bin/env python
"""reducer.py"""

from operator import itemgetter
import sys
current_followee =None
cur_follower_list = []
# input comes from STDIN

for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()

    # parse the input we got from mapper.py
    followee,follower = line.split('\t')
    if current_followee == followee:
        cur_follower_list.append(follower)
    else:
        
        if current_followee:
            if len(cur_follower_list) > 1:
                print '%s\t-\t%s' % (current_followee,1)
            else:
                print '%s\t-\t%s' % (current_followee,0)
        cur_follower_list = []
        cur_follower_list.append(follower)
        current_followee =followee
if current_followee:

    if len(cur_follower_list) > 1:
        print '%s\t-\t%s' % (current_followee,1)
    else:
        print '%s\t-\t%s' % (current_followee,0)