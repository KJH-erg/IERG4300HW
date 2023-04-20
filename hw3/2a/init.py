import random
with open('../MNIST/train_img') as f:
    data = f.read().split('\n')
centroids = []
for i in range(10):
    centroids.append(random.choice(data))
with open('centroid','w') as f:
    for i,j in zip(range(10),centroids):
        f.write('Centroid:'+str(i)+':'+'0:'+j+'\n')