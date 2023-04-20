#!/usr/bin/env python
import sys
import os
# read the centroid in dictionary in form of centroid ID:vectors 
with open ('fin','r') as f:
    data = f.read().split('\n')
    centroids = {}
    for i in data:
        try:
            values = i.split(':')
            centroids[values[1]]=values[3]
        except:
            pass
# mapper read data vectors + ground truth label
for item in sys.stdin:
    item = item.strip()
    distances = {}
    item_list = item.split(',')
# last part of data is ground truth label
    label= item_list[-1]
# other vectors for calculating distance
    item_list = item_list[0:-1]
# calculate distance for each centroid
    for key,vectors in centroids.items():
        vectors = vectors.split(',')
        distance = 0
        for i,j in zip(item_list,vectors):
            distance = distance+((float(i)-float(j))**2)
        distances[key] = distance
#find the minimum distance centroid ID
    min_key = min(distances, key=distances.get)
# output to reducer centroid ID with its ground truth label
    print(str(min_key)+'\t'+label)