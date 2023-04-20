
import numpy as np
from sklearn.preprocessing import StandardScaler
from scipy.linalg import eigh
from sklearn.decomposition import PCA

data= np.loadtxt("MNIST/train_img",
                 delimiter=",", dtype=float)
scaler = StandardScaler(with_mean=True, with_std=True)
data = scaler.fit_transform(data)
pca = PCA() # 주성분을 몇개로 할지 결정
pca.fit_transform(data)
print("Shape of eigen vectors = ",pca.components_.shape)
eigenvalues = pca.singular_values_
lst = [4, 8, 16, 32, 64]
for i in lst:
    print(np.sum(eigenvalues[:i]**2)/np.sum(eigenvalues**2))

    # converting the eigen vectors into (2,d) shape for easyness of further computations
    # with open("mnist/pca_components_"+str(i),'w') as f:
    #     for i in pca.components_:
    #         f.write(','.join(map(str, i.tolist()))+'\n')