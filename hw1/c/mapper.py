#!/usr/bin/env python
"""mapper.py"""

import sys
import os 
# input comes from STDIN (standard input)
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    # split the line into words
    line = line.split()
    followee = line[0]
    follower = line[1]
    print '%s\t%s' % (followee, follower)