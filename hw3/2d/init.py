import random
import os
with open('../MNIST/train_img') as f:
    data = f.read().split('\n')

lst = [12,15,20]
for n in lst:
    for i in range(1,4):
        centroids = []
        for j in range(n):
            centroids.append(random.choice(data))
        os.mkdir('./'+str(n)+'_'+str(i))
        with open('./'+str(n)+'_'+str(i)+'/init_centroid','w') as f, open('./'+str(n)+'_'+str(i)+'/centroid','w') as f2:
            for i,j in zip(range(n),centroids):
                f.write('Centroid:'+str(i)+':'+'0:'+j+'\n')
                f2.write('Centroid:'+str(i)+':'+'0:'+j+'\n')
        