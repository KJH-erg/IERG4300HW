#!/usr/bin/env python
"""reducer.py"""
import sys
import os 
current_item = None
for line in sys.stdin:
    line = line.strip()
    item,count = line.split('\t')
    if current_item != item:
        current_item =item
        print(item)
    else:
        pass