import sys
import os 
# input comes from STDIN (standard input)
for line in sys.stdin:
    line = line.strip()
    key,v = line.split(':')
    r,cnt = v.split('},')
    if re.search(p,key)
        print(key+'\t'cnt+'\t'+line)