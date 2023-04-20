#!/usr/bin/env python
import sys

current_key = None
current_value = '0'

for line in sys.stdin:
    line = line.strip()
    k1,k2,val = line.split("\t")
    if current_key != k1:
        if current_key:
            for k,v in tmp_dict.items():
                print(k+'\t'+current_key+'\t'+v+ ', ' +current_value)
        tmp_dict ={}
        current_key = k1
    if k2 == "-":
        current_value = (val.replace('{',''))
    else:
        tmp_dict[k2] = val
if current_key:
    for k,v in tmp_dict.items():
        print(k+'\t'+current_key+'\t'+v+ ', ' +current_value)