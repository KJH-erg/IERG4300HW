#!/usr/bin/env python
"""mapper2.py"""

import sys
import os 
for line in sys.stdin:
    line = line.strip()
    
    if line == "" :
        pass
    line = line.split()
    print('\t'.join(line))