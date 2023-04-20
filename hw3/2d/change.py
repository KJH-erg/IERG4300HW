lst = ['12_1','12_2','12_3','15_1','15_2','15_3','20_1','20_2','20_3']
#regex for searching ID only in centroid part
import re
p = re.compile("[0-9]+")
for n in lst:
# read the data after 2b stage containg major label from above
    with open('./' + n + '/'  + 'res2' ,'r') as f:
        data =f.read().split('\n')[0:-1]
    # write centroid ID with major label
    with open('./' + n + '/' + 'label','w') as f2:
            for i in data:
                sp = i.split()
                id = re.findall(p,sp[0])[0]
                f2.write(id+' '+sp[3]+'\n')