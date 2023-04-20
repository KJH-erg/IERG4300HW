#!/bin/bash
for d in 12_1 12_2 12_3 15_1 15_2 15_3 20_1 20_2 20_3
	do
		hadoop jar hadoop-streaming-2.10.1.jar \
		-D mapreduce.job.reduces=5 \
		-file /home/s1155096482/hw3/2d/$d/20 \
		-file ./test_mapper.py \
		-mapper ./test_mapper.py \
		-file ./test_reducer.py \
		-reducer ./test_reducer.py \
		-input /user/s1155096482/hw3/input/train_combined \
		-output /user/s1155096482/hw3/2d/${d}_res2 && \
        hadoop fs -cat /user/s1155096482/hw3/2d/${d}_res2/* > /home/s1155096482/hw3/2d/$d/${d}_res2
	done
