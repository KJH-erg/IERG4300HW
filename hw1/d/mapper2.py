#!/usr/bin/env python
"""mapper2.py"""

import sys
import os 
# input comes from STDIN (standard input)
for line in sys.stdin:
    line = line.strip()
    if line =="":
        pass
    else:
        print(line)