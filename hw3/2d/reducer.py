#!/usr/bin/env python
import sys
import os

tmp_dict={}
for line in sys.stdin:
    line = line.strip()
    key,lst=line.split('\t')
    lst = lst.split(',')
    saved_data = tmp_dict.get(key,(0,[0]*784))
    cnt = saved_data[0]+1
    fin_list = []
    for i,j in zip(saved_data[1],lst):
        fin_list.append(int(i)+int(j))
    tmp_dict[key] = (cnt,fin_list)
for k,v in tmp_dict.items():
    cnt = v[0]
    lst = v[1]
    fin_lst = []
    for i in lst:
        fin_lst.append(float(i)/cnt)
    print 'Centroid:'+k+':'+str(cnt)+':'+",".join(format(x, ".7f") for x in fin_lst)