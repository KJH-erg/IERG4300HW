with open ('./seed2/15','r') as f:
    data =f.read().split('\n')
with open('res','w') as f:
    for i in data[0:-1]:
        t = i.split(':')
        f.write("Centroid"+t[1]+':'+t[2]+",["+t[3]+']\n')