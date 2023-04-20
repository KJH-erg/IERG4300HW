#!/usr/bin/env python
# check_reducer.py
import sys
import os
# save each centroid ID with its predicted label
# in dictionary form
label ={}
with open ('label','r') as f:
    data = f.read().split('\n')
    for i in data:
        try:
            values = i.split(' ')
            label[values[0]]=values[1]
        except:
            pass
total_cnt=0
correct_cnt=0
current_dict = {}
current_key = 0
for line in sys.stdin:
    line = line.strip()
    key,actual = line.split('\t')
# if key(centorid ID) is same with before
    if current_key == key:
# count the total count for each centroid
        total_cnt+=1
# if ground_truth label equals to predicted label
        if (label[key] == actual):
            correct_cnt+=1
# if there is a new key(centroid ID)
# reset to the 0 counts
    else:
# print the previous centroid ID's result
        if current_key:
            print('Centroid' + current_key +' label is '+ label[current_key] + ' count is ' + str(total_cnt) +' correct is '+str(correct_cnt)+' accuracy is ' + str((float(correct_cnt)/total_cnt)))
        current_key = key
        total_cnt=1
        correct_cnt=0
        if (label[key] == actual):
            correct_cnt+=1
# do not forget to output the last key
if current_key == key:
    print('Centroid' + current_key +' label is '+ label[current_key] + ' count is ' + str(total_cnt) +' correct is '+str(correct_cnt)+' accuracy is ' + str((float(correct_cnt)/total_cnt)))