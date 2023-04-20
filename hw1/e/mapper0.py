#!/usr/bin/env python
import re

"""mapper.py"""
import sys
import os 
for line in sys.stdin:
    line = line.strip()
    line = line.split()
    followee = line[0]
    follower = line[1]
    print '%s\t%s' % (followee, follower)