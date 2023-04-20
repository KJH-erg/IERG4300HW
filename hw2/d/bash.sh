#!/bin/bash
time hadoop jar hadoop-streaming-2.10.1.jar \
  -D mapreduce.job.reduces=5 \
	-file ./mapper.py \
	-mapper ./mapper.py \
	-file ./reducer.py \
	-reducer ./reducer.py \
  -input /user/s1155096482/hw2/input/yelp_review \
  -output /user/s1155096482/hw2/d/pass1 &&
    hadoop fs -cat /user/s1155096482/hw2/d/pass1/* > freq_items &&
  time hadoop jar hadoop-streaming-2.10.1.jar \
  -D mapreduce.job.reduces=10 \
	-file ./freq_items \
	-file ./mapper2.py \
	-mapper ./mapper2.py \
	-file ./reducer2.py \
	-reducer ./reducer2.py \
  -input /user/s1155096482/hw2/input/yelp_review \
  -output /user/s1155096482/hw2/d/pass2
