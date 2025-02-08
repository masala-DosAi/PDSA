edges = [(1, 2), (1, 3), (2, 4), (3, 4), (4, 5)]
import numpy as np
A=np.zeros(shape=(10,10))
for (i,j) in edges:
    A[i][j]=1
print(A)