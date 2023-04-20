#!/usr/bin/env python
import sys
from operator import itemgetter

current_comm = None
current_count = 0
comm = None

# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()

    # parse the input we got from mapper.py
    comm, count = line.split('\t', 1)

    # convert count (currently a string) to int
    try:
        count = int(count)
    except ValueError:
        # count was not a number, so silently
        # ignore/discard this line
        continue

    # this IF-switch only works because Hadoop sorts map output
    # by key (here: word) before it is passed to the reducer
    if current_comm == comm:
        current_count += count
    else:
        if current_comm:
            # write result to STDOUT
            print 'Commmunity %s: %s' % (current_comm, current_count)
        current_count = count
        current_comm = comm

# do not forget to output the last word if needed!
if current_comm == comm:
    print 'Community %s: %s' % (current_comm, current_count)