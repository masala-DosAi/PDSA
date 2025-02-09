edges = [(1,2),(2,3),(2,4)]
import numpy as np
A=np.zeros(shape=(5,5))
for (i,j) in edges:
    A[i][j]=1
print(A)