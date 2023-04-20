#!/usr/bin/env python
"""mapper2.py"""
import re
p = re.compile(".*6482$")

import sys
import os 
# input comes from STDIN (standard input)
for line in sys.stdin:
    line = line.strip()
    print(line)