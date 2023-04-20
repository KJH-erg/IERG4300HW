#!/bin/bash
for d in 4 8 16 32 64
	do
		hadoop jar hadoop-streaming-2.10.1.jar \
			-D mapreduce.job.reduces=5 \
			-file /home/s1155096482/hw4/$d/20 \
			-file /home/s1155096482/hw4/$d/label \
			-file ./check_mapper.py \
			-mapper ./check_mapper.py \
			-file ./check_reducer.py \
			-reducer ./check_reducer.py \
			-input /user/s1155096482/hw4/input/test_combined_$d \
			-output /user/s1155096482/hw4/$d/res && \
		hadoop fs -cat /user/s1155096482/hw4/$d/res/* > /home/s1155096482/hw4/$d/res
done