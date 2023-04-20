#!/bin/bash
for d in 4 8 16 32 64
  do
    for i in $(seq 20 $END)
    do
      hadoop jar hadoop-streaming-2.10.1.jar \
        -D mapreduce.job.reduces=5 \
        -D mapred.map.tasks=5 \
      -D mapred.min.split.size=435456 \
      -file /home/s1155096482/hw4/$d/centroid \
      -file ./mapper.py \
        -mapper ./mapper.py \
        -file ./reducer.py \
        -reducer ./reducer.py \
        -input /user/s1155096482/hw4/input/train_${d} \
        -output /user/s1155096482/hw4/$d/$i && \
      hadoop fs -cat /user/s1155096482/hw4/$d/$i/* > /home/s1155096482/hw4/$d/$i && \
      hadoop fs -cat /user/s1155096482/hw4/$d/$i/* > /home/s1155096482/hw4/$d/centroid
    done
  done
