#!/bin/bash
for d in 12_1 12_2 12_3 15_1 15_2 15_3 20_1 20_2 20_3
	do
	hadoop jar hadoop-streaming-2.10.1.jar \
			-D mapreduce.job.reduces=5 \
			-file /home/s1155096482/hw3/2d/$d/20 \
			-file /home/s1155096482/hw3/2d/$d/label \
			-file ./check_mapper.py \
			-mapper ./check_mapper.py \
			-file ./check_reducer.py \
			-reducer ./check_reducer.py \
			-input /user/s1155096482/hw3/input/test_combined \
			-output /user/s1155096482/hw3/2d/${d}_fin && \
		hadoop fs -cat /user/s1155096482/hw3/2d/${d}_fin/* > /home/s1155096482/hw3/2d/${d}_fin
done