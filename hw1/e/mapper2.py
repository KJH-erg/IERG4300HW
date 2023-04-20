#!/usr/bin/env python
"""mapper2.py"""
import sys
import os 
import ast
from itertools import combinations
lst = ['100617619899910326482',	
'100680316115587656482'	,
'102947638698342246482'	,
'103515743035978486482'	,
'104762014074114156482',
'105082921745042856482'	,
'109053536936436896482'	,
'110972858183646806482'	,
'111633927555221496482'	,
'113751831138079026482'	,
'114056321367305046482'	,
'114528278590085046482']
tmp={}
for line in sys.stdin:
    line = line.strip()
    line = line.split('\t')
    followee = line[0]
    followers = list(line[1].split(','))
    for i in lst:
        if i in followers:  
            pairs = []
            for k in followers:
                if i != k:
                    pairs.append((i,k))
            for j in pairs:
                print '%s\t%s\t%s\t%s' % ((j[0]),(j[1]),followee,1)