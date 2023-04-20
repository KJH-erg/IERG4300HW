#1A
import numpy as np
from numpy import dot
from numpy.linalg import norm
A = np.array([
[1,1, 1, 0, 0],
[3, 3, 3, 0, 0],
[4, 4, 4, 0, 0],
[5, 5, 5, 0, 0],
[0, 2, 0, 4, 4],
[0, 0, 0, 5, 5],
[0, 1, 0, 2, 2]])
# print(A.shape)
U, D, VT = np.linalg.svd(A, full_matrices=False)
print(U)
# print(D)
# print(VT)
print(U[:,:2])