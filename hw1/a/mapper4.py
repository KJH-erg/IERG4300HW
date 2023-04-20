#!/usr/bin/env python
"""mapper2.py"""
import sys
import os 
import ast
from itertools import combinations
tmp={}
for line in sys.stdin:
    line = line.strip()
    if line =='':
        pass
    pair1,r = line.split(':')
    pair2,values = r.split(' ',1)
    print(pair1+'\t'+pair2+"\t"+values)

