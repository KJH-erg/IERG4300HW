#!/bin/bash
for d in 4 8 16 32 64
  do
	hadoop jar hadoop-streaming-2.10.1.jar\
      -D mapreduce.job.reduces=5 \
		-D mapred.map.tasks=5 \
      	-D mapred.min.split.size=435456 \
		-file /home/s1155096482/hw4/$d/20 \
		-file ./test_mapper.py \
		-mapper ./test_mapper.py \
		-file ./test_reducer.py \
		-reducer ./test_reducer.py \
        -input /user/s1155096482/hw4/input/train_combined_${d} \
        -output /user/s1155096482/hw4/${d}/fin && \
      hadoop fs -cat /user/s1155096482/hw4/${d}/fin/* > /home/s1155096482/hw4/$d/fin
  done
