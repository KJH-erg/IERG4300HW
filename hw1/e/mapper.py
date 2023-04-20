#!/usr/bin/env python
"""mapper.py"""
import sys

for line in sys.stdin:
    data,count = line.strip().split('},')

    count = count.strip()
    print ((count)+'\t'+data+'},')