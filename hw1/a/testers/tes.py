#!/usr/bin/env python
import math
import operator as op
from functools import reduce
import sys
import ast
# def ncr(n, r):
#     if n == 1:
#         return 0
#     r = min(r, n-r)
#     numer = reduce(op.mul, range(n, n-r, -1), 1)
#     denom = reduce(op.mul, range(1, r+1), 1)
#     return numer / denom  # or / in Python 2
# print(ncr(4,2))
# with open ('medium_inter.txt') as f:
#     data = f.read()
# data = data.split('\n')
# cnt = 0
# for i in data[0:-1]:

#     tmp = ast.literal_eval(i.split('\t')[1])
#     cnt+=(ncr(len(tmp), 2))
# print(cnt)

# with open ('medium.txt') as f:
#     data = f.read()
# data = data.split('\n')
# cnt2=0
# for i in data[0:-1]:
#     try:
#         t=i.split('},')[1]
#         t = t.strip()
#         t =int(t)
#         cnt2+=t
#     except:
    
#         print(i)
# #         # sys.exit(0)
# print(cnt2)
# import ast
# with open ('medium_inter.txt') as f:
#     data = f.read()
# data = data.split('\n')
# cnt3=0
# for i in data[0:-1]:
#     t = len(ast.literal_eval(i.split('\t')[1]))
#     cnt3+=t
# print(cnt3)

# with open ('a.txt') as f:
#     data = f.read()
# data = data.split('\n')
# lst= []
# for i in data:
#     lst.append(i.split(':')[0])

# with open ('/home/s1155096482/medium/medium_label') as f:
#     data = f.read()
# data = data.split('\n')
# lst2= []
# for i in data:
#     lst2.append(i.split(' ')[0])

# print(set(lst2)-set(lst))

with open ('medium.txt') as f:
    data = f.read()
data = data.split('\n')
lst3 =[]
vs = ['97036482',
'399156482',
'302936482',
'403956482',
'756482',
'22426482',
'121296482',
'40026482',
'145356482',]
for v in vs:
    lst3=[]
    for i in data[0:-1]:

        try:
            k,d = i.split(':')
            if k == v:
                t=i.split('},')[1]
                t = t.strip()
                t =int(t)
                lst3.append(t)
        except:
            print(i)
    print(max(lst3))