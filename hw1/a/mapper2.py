#!/usr/bin/env python
"""mapper2.py"""
import sys
import os 
import ast
from itertools import combinations
tmp={}
for line in sys.stdin:
    line = line.strip()
    line = line.split('\t')
    followee = line[0]
    followers = ast.literal_eval(line[1])
    pairs = list(combinations(followers, 2))
    for i in pairs:
        i = sorted(i)
        print '%s\t%s\t%s\t%s' % (int(i[0]),int(i[1]),followee,1)