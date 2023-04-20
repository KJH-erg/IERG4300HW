#!/usr/bin/env python
"""reducer.py"""

from operator import itemgetter
import sys
current_follower =None
cur_followee_list = []
# input comes from STDIN

for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()

    # parse the input we got from mapper.py
    follower,followee = line.split('\t')
    if current_follower == follower:
        cur_followee_list.append(followee)
    else:
        if current_follower:
            print '%s\t-\t{%s' % (current_follower, len(cur_followee_list))
        cur_followee_list = []
        cur_followee_list.append(followee)
        current_follower =follower
print '%s\t-\t{%s' % (current_follower,len(cur_followee_list))