#!/usr/bin/env python
import sys
import os
import math
# read 10 centroids 
with open ('centroid','r') as f:
# for all centroids
    centroids = f.read().split('\n')
    centroid_IDs = {}
# for each centroid
    for i in centroids:
# exception handling for empty line
        try:
            values = i.split(':')
# values[1] for centroid ID values[3] for data vector
            centroid_IDs[values[1]]=values[3]
        except:
            pass
# for each train data item
for item in sys.stdin:
    item = item.strip()
# save all disatances from 10 centroids
    distances = {}
# one train data into list
    item_list = item.split(',')
# for all centroids    
    for key,vectors in centroid_IDs.items():
        vectors = vectors.split(',')
        distance = 0
# calculate distance
        for i,j in zip(item_list,vectors):
            distance = distance+((float(i)-float(j))**2)
# save distance in dictionary
        distances[key] = math.sqrt(distance)
# find mininum distance and find its key (centroid index)
    min_key = min(distances, key=distances.get)
    # print(distances)
# print centroid key with one train data vectors    
    print(str(min_key)+'\t'+item)