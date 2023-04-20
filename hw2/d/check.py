with open ('yelp_review',"r") as f:
    data = f.read().split('\n')
# import ast
lst1 = ['AM','American','Because','Caesars','English','Food','Got','Grill','House','Im','Las','Now','ONLY','Pizza']
cnt=0
for j in lst1:
    cnt=0
    for i in data[0:-1]:
        items = i.split()
        if '1000' in items and j in items:
            cnt+=1

    
    
    print(cnt)  