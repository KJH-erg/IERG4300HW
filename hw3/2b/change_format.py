lst = ['seed2']
for d in lst:
    with open("./"+d+'/'+d, "r") as f:
        centorids = f.read().split('\n')[0:-1]
    with open("./"+d+'/centroid', "w") as f:
        for i,j in zip(range(10),centorids):
            f.write('Centroid:'+str(i)+':'+'0:'+j+'\n')