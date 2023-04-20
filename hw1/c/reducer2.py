#!/usr/bin/env python
import sys

current_key = None
current_value = 0
is_label = False
current_label = None
tmp ={}

for line in sys.stdin:
    line = line.strip()
    data = line.split()
    flag = len(data)
    if flag == 2:
        k = data[0]
        is_label = True
        label = data[1]
    else:
        k = data[0]
        is_label = False
        value = int(data[2])
    cnt,tmp_label = tmp.get(k,(0,None))
    if is_label:
        tmp_label = label
    else:
        cnt+=value
    tmp[k]= (cnt,tmp_label)
for k,v in tmp.items():
    print(v[1]+'\t'+str(v[0]))
