#!/bin/bash
for d in  seed2
  do
    for i in $(seq 20 $END)
    do
      hadoop jar hadoop-streaming-2.10.1.jar \
        -D mapreduce.job.reduces=5 \
        -D mapred.map.tasks=5 \
      -D mapred.min.split.size=435456 \
      -file /home/s1155096482/hw3/2b/$d/centroid \
      -file ./mapper.py \
        -mapper ./mapper.py \
        -file ./reducer.py \
        -reducer ./reducer.py \
        -input /user/s1155096482/hw3/input/train_img \
        -output /user/s1155096482/hw3/2b/$d/$i && \
      hadoop fs -cat /user/s1155096482/hw3/2b/$d/${i}/* > /home/s1155096482/hw3/2b/$d/$i && \
      hadoop fs -cat /user/s1155096482/hw3/2b/$d/${i}/* > /home/s1155096482/hw3/2b/$d/centroid
    done
  done
