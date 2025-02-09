class Queue:
    def __init__(self):
        self.queue = []  # Using a list
    
    def addq(self, v):
        self.queue.append(v)
    
    def delq(self):
        if not self.isempty():
            return self.queue.pop(0)  # Efficiently removes and returns the first element
        return None
    
    def isempty(self):
        return len(self.queue) == 0
    
    def __str__(self):
        return str(self.queue)


def bfs(A, v):  # Fixed function name (was incorrectly named DFS)
    visited = {node: False for node in A}
    parent = {}
    q = Queue()

    visited[v] = True
    q.addq(v)

    while not q.isempty():
        j = q.delq()
        for k in A.get(j, []):
            if not visited[k]:
                visited[k] = True
                parent[k] = j
                q.addq(k)
    
    return visited


def lister(A):
    D={}
    for x in A:
        if x[0] in D:
            D[x[0]].append(x[1])
            print(D)
        else:
            D[x[0]]=[x[1]]
    return D


# Directed graph as a list of edges
A = [(1, 2), (2, 3), (2, 4)]
def get_list(A,x):
    l=[]
    d=bfs(lister(A),x)
    for y in d:
        if d[y]==True:
            l.append(y)
    return l
print(get_list(A,1))