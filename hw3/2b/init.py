import random
with open('../MNIST/train_img') as f:
    data = f.read().split('\n')[0:-1]

lst = [1,2]
for n in lst:
    centroids = []
    for j in range(10):
        centroids.append(random.choice(data))
        
    with open('./'+str(n)+'/init_centroid','w') as f, open('./'+str(n)+'/centroid','w') as f2:
        for i,j in zip(range(10),centroids):
            f.write('Centroid:'+str(i)+':'+'0:'+j+'\n')
            f2.write('Centroid:'+str(i)+':'+'0:'+j+'\n')
    