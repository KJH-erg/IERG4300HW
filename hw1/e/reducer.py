#!/usr/bin/env python
"""reducer.py"""

from operator import itemgetter
import sys

# input comes from STDIN

for line in sys.stdin:
    line = line.strip()
    cnt,data = line.split('\t')
    print(data+cnt)