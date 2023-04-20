
import numpy as np
from sklearn.preprocessing import StandardScaler
from scipy.linalg import eigh
from sklearn.decomposition import PCA

data= np.loadtxt("MNIST/train_img",
                 delimiter=",", dtype=float)
scaler = StandardScaler(with_mean=True, with_std=True)
data = scaler.fit_transform(data)
pca = PCA() 
pca.fit_transform(data)
# print("Shape of eigen vectors = ",pca.components_.shape)
lst = [4, 8, 16, 32, 64]
for i in lst:
#     # converting the eigen vectors into (2,d) shape for easyness of further computations
    with open("MNIST/pca_components_"+str(i),'w') as f:
        for j in pca.components_[0:i]:
            f.write(','.join(map(str, j.tolist()))+'\n')