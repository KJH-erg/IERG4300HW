#!/usr/bin/env python
import sys
def clean(v):
    _,intersection,pair1 = (v.split('}')[1].split(','))
    value = v.split('}')[0]+'}'
    return value, intersection,pair1
def calculate_sim(v1,v2,intersection):
    union = int(v1)+int(v2)-int(intersection)

    return float(intersection)/union

import sys

current_key = None
current_value = '0'

for line in sys.stdin:
    line = line.strip()
    k1,k2,val = line.split("\t")
    if current_key != k1:
        if current_key:
            for k,v in tmp_dict.items():
                common_followee,intersection,pair1 = clean(v)
                print(k+':'+current_key+','+common_followee+ ',' +'%.05f' %(calculate_sim(pair1,current_value,intersection)))
        tmp_dict ={}
        current_key = k1
    if k2 == "-":
        current_value = (val.replace('{',''))
    else:
        tmp_dict[k2] = val

if current_key:
    for k,v in tmp_dict.items():
        common_followee,intersection,pair1 = clean(v)
        print(k+':'+current_key+','+common_followee+ ',' + '%.05f' %(calculate_sim(pair1,current_value,intersection)))