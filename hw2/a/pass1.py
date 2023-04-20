#!/usr/bin/env python
# dictionary used for saving counts
hash_count={}
# saving total basket counts
total_basket_number = 0
# threshold
thres = 0.01
#read input file
with open ('yelp_review','r') as f:
    data = f.read()
# split by \n and [0:-1] for removing last empty line
data = data.split('\n')[0:-1]
#loop for each basket
for basket in data[0:100]:
    basket = basket.strip()
    items = basket.split()
# split items into items
    for item in items:
# add 1 to count for certain item and save to dictionary
        tmp_cnt = hash_count.get(item,0)
        tmp_cnt = tmp_cnt+1
        hash_count[item] = tmp_cnt
    total_basket_number=total_basket_number+1
# After looping all baskets
# if each item saved in dictionary is greater than threshold save the result
with open("pass1.txt",'w') as f:
    for item,count in hash_count.items():
        cur_p = (float(count)/float(total_basket_number))
        if cur_p >= thres:
            f.write(item+'\n')