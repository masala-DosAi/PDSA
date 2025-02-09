#this code is being used to create a adjancency matrix from the given edges of a graph in the form of a list
edges = [(1, 2), (1, 3), (2, 4), (3, 4), (4, 5)]
import numpy as np
A=np.zeros(shape=(10,10))
for (i,j) in edges:
    A[i][j]=1
print(A)



#this code is being used to identify the neighbours of a given node 
def neighbours(A,i):
    nbrs=[]
    (rows,cols)=A.shape
    for j in range(cols):
        if A[i][j]==1:
            nbrs.append(j)
    return nbrs

print(neighbours(A,2))