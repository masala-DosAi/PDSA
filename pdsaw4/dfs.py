A=[
    [0., 0., 0., 0., 0.],
    [0., 0., 1., 0., 0.],
    [0., 0., 0., 1., 1.],
    [0., 0., 0., 0., 0.],
    [0., 0., 0., 0., 0.]
]
def neighbours(A,i):
    nbrs=[]
    (rows,cols)=len(A),len(A)
    for j in range(cols):
        if A[i][j]==1:
            nbrs.append(j)
    return nbrs

visited,parent={},{}
def DFSinit(A):
    rows=len(A)
    for i in range(rows):
        visited[i]=False
        parent[i]=-1
    return


def DFS(A,v):
    visited[v]=True
    print(visited)
    for x in neighbours(A,v):
        if not visited[x]:
            parent[x]=v
        DFS(A,x)
    return parent
    
print(DFS(A,3))