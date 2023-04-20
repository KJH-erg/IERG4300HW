import numpy as np
import math
from numpy.linalg import norm
M = np.array([[5, 4, 2, 0,3, 1, 2],[2, 5, 3, 4, 0,2,0],[0,0,1,2, 4, 5, 3],[3,0,0, 4, 2, 1, 4],[2, 4, 5,0,1,0, 4]])
# for i in range(1,5):
#     my_rho = np.corrcoef(M[0], M[i])
#     # print(my_rho)
#     pearson = ((M[0]-np.mean(M[0]))@(M[i]-np.mean(M[i])))/(math.sqrt(np.sum((M[0]-np.mean(M[0]))**2)*np.sum((M[i]-np.mean(M[i]))**2)))
#     print(pearson)
# # 2,5
# #sim = 4 , 0

# M = np.array([[1,0, 3, 0 , 0, 5,0,0 ,5,0 ,4,0],[0,0,5, 4,0,0, 4,0,0, 2, 1, 3],[2, 4,0, 1, 2, 0,3,0 ,4 ,3, 5,0],[0,2 ,4,0 ,5,0,0, 4,0,0, 2,0],[0,0,4 ,3 ,4, 2,0,0,0,0, 2, 5],[1, 0,3,0 ,3,0,0, 2,0,0, 4,0]])
print(M.shape)
for i in range(0,5):
    A = []
    nz =(M[0][np.nonzero(M[0])])
    avg = np.mean(nz)
    # print(avg)
    for j in M[0]:
        if j!=0:
            A.append(j-avg)
        else:
            A.append(0)
    B = []
    nz =(M[i][np.nonzero(M[i])])
    avg = np.mean(nz)
    for j in M[i]:
        if j!=0:
            B.append(j-avg)
        else:
            B.append(0)
    cosine = np.dot(A,B)/(norm(A)*norm(B))
    # print(A)
    print(cosine)