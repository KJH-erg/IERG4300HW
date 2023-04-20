#!/bin/bash
for d in 12_1 12_2 12_3 15_1 15_2 15_3 20_1 20_2 20_3
  do
    for i in $(seq 20 $END)
    do
      hadoop jar hadoop-streaming-2.10.1.jar \
        -D mapreduce.job.reduces=5 \
        -D mapred.map.tasks=5 \
      -D mapred.min.split.size=435456 \
      -file /home/s1155096482/hw3/2d/$d/centroid \
      -file ./mapper.py \
        -mapper ./mapper.py \
        -file ./reducer.py \
        -reducer ./reducer.py \
        -input /user/s1155096482/hw3/input/train_img \
        -output /user/s1155096482/hw3/2d/$d/$i && \
      hadoop fs -cat /user/s1155096482/hw3/2d/$d/${i}/* > /home/s1155096482/hw3/2d/$d/$i && \
      hadoop fs -cat /user/s1155096482/hw3/2d/$d/${i}/* > /home/s1155096482/hw3/2d/$d/centroid
    done
  done

