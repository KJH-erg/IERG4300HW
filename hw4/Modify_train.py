import numpy as np
lst = [4,8,16,32,64]
datas = np.loadtxt("MNIST/train_img",
                 delimiter=",", dtype=float)
for i in lst:
    pca = np.loadtxt("MNIST/pca_components_"+str(i), delimiter=",", dtype=float)
    print(pca.T.shape)
    res = np.dot(datas,pca.T)
    print(np.dot(datas[0],pca.T))
    with open('result_train_2/train_'+str(i),"w") as f:
        for j in res:
            f.write(','.join(map(str, j.tolist()))+'\n')
            
datas = np.loadtxt("new_seed/random_seed_1",
                 delimiter=",", dtype=float)   
for i in lst:
    pca = np.loadtxt("MNIST/pca_components_"+str(i), delimiter=",", dtype=float)
    print(pca.T.shape)
    res = np.dot(datas,pca.T)
    print(np.dot(datas[0],pca.T))
    with open('result_train_2/seed_'+str(i),"w") as f:
        for j in res:
            f.write(','.join(map(str, j.tolist()))+'\n')
    
    