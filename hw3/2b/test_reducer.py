#!/usr/bin/env python
import sys
import os
current_dict = {}
current_key = 0
for line in sys.stdin:
    line = line.strip()
    key,actual = line.split('\t')
# if key(centorid ID) is same
# count the count for each ground truth label  
    if current_key == key:
        
        tmp = current_dict.get(actual,0)
        current_dict[actual] = tmp+1
        # print(actual)
# if there is a new key(centroid ID)
    else:
        if current_key:
# find the maximum count of ground truth label
            max_key = max(current_dict, key=current_dict.get)
# print the final result centroid ID max ground truth label
#  sum(current_dict.values() is for sum of all ground truth label count
# accuracy = max count of certain ground truth label /sum of all ground truth label count
            print(max_key)
            print(current_dict)
            print('Centroid' + current_key +' label is '+ max_key + ' count is ' + str(sum(current_dict.values())) +' correct is '+str(current_dict[max_key])+' accuracy is ' + str(float(current_dict[max_key])/sum(current_dict.values())))
# for new key(centroid ID), initialize        
        current_key = key
        current_dict = {}
        tmp = current_dict.get(actual,0)
        current_dict[actual] = tmp+1
  
# do not forget to output the last key
if current_key == key:
    print(max_key)
    print(current_dict)
    max_key = max(current_dict, key=current_dict.get)
    print('Centroid' + current_key +' label is '+ max_key + ' count is ' + str(sum(current_dict.values())) +' correct is '+str(current_dict[max_key])+' accuracy is ' + str(float(current_dict[max_key])/sum(current_dict.values())))