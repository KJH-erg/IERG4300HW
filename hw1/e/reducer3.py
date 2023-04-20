#!/usr/bin/env python
"""reducer2.py"""

import sys
labels = {}
with open('all_label') as f:
    data = f.read()
for i in data.split('\n')[0:-1]:
    k,v = i.split('\t')
    labels[k] = v
# input comes from STDIN
for line in sys.stdin:
    line = line.strip()
    key_follower, a= line.split(':')
    key_follower = key_follower.strip()
    paired_follower,b = a.split('{')
    paired_follower = paired_follower.strip()
    common_followee,count = b.split('},')
    common_followee = common_followee.strip()
    count = count.strip()
    union = int(labels[key_follower])+int(labels[paired_follower])-int(count)
    sim = float(count)/union
    print(key_follower+':'+paired_follower+" {"+common_followee +'}, ' "%0.5f" %sim )