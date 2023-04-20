#!/bin/bash
for i in $(seq 1 $END)
do
    # hadoop jar hadoop-streaming-2.10.1.jar \
    # -D mapreduce.job.reduces=5 \
    # -D mapred.map.tasks=5 \
    # -D mapred.min.split.size=435456 \
    # -file /home/s1155096482/hw3/2a/centroid \
    # -file ./mapper.py \
    # -mapper ./mapper.py \
    # -file ./reducer.py \
    # -reducer ./reducer.py \
    # -input /user/s1155096482/hw3/input/train_img \
    # -output /user/s1155096482/hw3/2a/$i && \
    # hadoop fs -cat /user/s1155096482/hw3/2a/$i/* > /home/s1155096482/hw3/2a/centroid &&\
    hadoop fs -cat /user/s1155096482/hw3/2a/$i/* > /home/s1155096482/hw3/2a/centroids/$i 
done