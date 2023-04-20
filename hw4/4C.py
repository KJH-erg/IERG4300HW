import numpy as np

def matrix_factorization(R, P, Q, K, steps=5000, alpha=0.0002, beta=0.02):
    Q = Q.T
    for step in range(steps):
        for i in range(len(R)):
            for j in range(len(R[i])):
                if R[i][j] > 0:
                    eij = R[i][j] - np.dot(P[i,:],Q[:,j])
                    for k in range(K):
# bug location and bug correction together
                        tmp_p = P[i][k] + alpha * (2 * eij * Q[k][j] - beta * P[i][k])
                        tmp_q = Q[k][j] + alpha * (2 * eij * P[i][k] - beta * Q[k][j])
                        P[i][k] = tmp_p
                        Q[k][j] = tmp_q
                        
        eR = np.dot(P,Q)
        e = 0
        for i in range(len(R)):
            for j in range(len(R[i])):
                if R[i][j] > 0:
                    e = e + pow(R[i][j] - np.dot(P[i,:],Q[:,j]), 2)
                    for k in range(K):
                        e = e + (beta/2) * (pow(P[i][k],2) + pow(Q[k][j],2))
        if e < 0.001:
            break
    return P, Q.T

R = np.array([[5, 4, 2, 0,3, 1, 2],[2, 5, 3, 4, 0,2,0],[0,0,1,2, 4, 5, 3],[3,0,0, 4, 2, 1, 4],[2, 4, 5,0,1,0, 4]])
R = np.array(R)
N = len(R)
M = len(R[0])
K = 3
P = np.random.rand(N,K)
Q = np.random.rand(M,K)

nP, nQ = matrix_factorization(R, P, Q, K)
nR = np.dot(nP, nQ.T)

#print user1 restarant D
print(nR[0,3])