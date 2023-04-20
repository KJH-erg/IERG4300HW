lst = ['4','8','16','32','64']
#regex for searching ID only in centroid part
import re
p = re.compile("[0-9]+")
for n in lst:
# read the data after 2b stage containg major label from above
    with open('./' + n + '/'  + 'fin' ,'r') as f:
        data =f.read().split('\n')[0:-1]
    # write centroid ID with major label
    with open('./' + n + '/' + 'label','w') as f2:
        for i in data:
            sp = i.split()
            id = re.findall(p,sp[0])[0]
            f2.write(id+' '+sp[3]+'\n')