#!/bin/bash
for d in seed2
	do
		hadoop jar hadoop-streaming-2.10.1.jar \
		-D mapreduce.job.reduces=5 \
		-D mapred.map.tasks=5 \
      	-D mapred.min.split.size=435456 \
		-file /home/s1155096482/hw3/2b/$d/15 \
		-file ./test_mapper.py \
		-mapper ./test_mapper.py \
		-file ./test_reducer.py \
		-reducer ./test_reducer.py \
		-input /user/s1155096482/hw3/input/train_combined \
		-output /user/s1155096482/hw3/2b/${d}/fin && \
        hadoop fs -cat /user/s1155096482/hw3/2b/${d}/fin/* > /home/s1155096482/hw3/2b/$d/fin &&
        sort /home/s1155096482/hw3/2b/$d/${d}/fin/* > /home/s1155096482/hw3/2b/$d/fin2
	done