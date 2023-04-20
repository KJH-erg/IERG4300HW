#1A
import numpy as np
from numpy import dot
from numpy.linalg import norm
A = np.array([[4,2,5,5,3,4],[5,5,3,1,4,3],[4,2,4,5,1,5],[5,4,1,3,5,2],[2,3,5,4,3,5]])
# print(A.shape)
U, D, VT = np.linalg.svd(A, full_matrices=False)
# print(U)
# print(D)
# print(VT)
# print(U[:,:2])
# print(D[0:2])
# print(VT[0:2])
# #1B
reduced = (VT[0:2])
student_6 = np.array([4,3,4,5,5,2])
# print(student_6@reduced.T)
# # #1C

student_3= [4,2,4,5,1,5]
student_5 = [2,3,5,4,3,5]
cos_sim = dot(student_3, student_5)/(norm(student_3)*norm(student_5))
# print(cos_sim)

new_3 = (student_3@reduced.T)
new_5 =(student_5@reduced.T)
print(new_3)
print(new_5)
cos_sim = dot(new_3, new_5)/(norm(new_3)*norm(new_5))
print(cos_sim)