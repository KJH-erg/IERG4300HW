with open ('e_fin2.txt') as f:
    data = f.read()
for i in data.split('\n'):
    k,v=i.split("},")
    k1,k2 = k.split('{')
    lst = k2.split(',')
    print(k1+' {' + ','.join(lst[0:10])+ '...} ' +v)