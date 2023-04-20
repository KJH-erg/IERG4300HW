with open("commons.txt")as f:
    data = f.read()
data = data.split('\n')[0:-1]
import sys
for i in data:
    k1,k2, v= i.split('\t')
    if k1 =="34428387" and k2 =="22462187":
        print(v)
