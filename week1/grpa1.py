#inputs are L&P and sadly this code is only passing 4 private tests
def find_Min_Difference(L,P):
    l=sorted(L)
    sub=[]
    val=[]
    x=0
    y=P
    while len(l)!=y:
        sub.append(l[x:y])
        l=l[x+1:]
    
    for t in sub:
        z=max(t)-min(t)
        val.append(z)
    return sorted(val)[0]def find_Min_Difference(L,P):
#approach 2 and this code is the actual answer and passes all 5 private tests
def find_Min_Difference(L,P):
  L.sort()
  N = P
  M = len(L)
  min_diff = max(L) - min(L)
  for i in range(M-N+1):
    if L[i+N-1] - L[i] < min_diff:
      min_diff = L[i+N-1] - L[i]
  return min_diff

