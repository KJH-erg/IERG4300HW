import math
distances = []
prev = {}
with open ('./centroids/1','r') as f:
    data = f.read().split('\n')[:-1]
    for i in data:
        i = i.split(':')
        k,v = (i[1],i[3])
        prev[k] = v
for i in range(2,21):
    with open ('./centroids/'+str(i),'r') as f:
        new = {}
        data = f.read().split('\n')[:-1]
        for i in data:
            i = i.split(':')
            k,v = (i[1],i[3])
            new[k] = v
        distance = 0
        for i in range(10):
            p = prev[str(i)].split(',')
            n = new[str(i)].split(',')
            for pi,ni in zip(p,n):
                distance = distance +(float(pi)-float(ni))**2
        distances.append(math.sqrt(distance))
        prev = new.copy()
print(distances)

            
        
        