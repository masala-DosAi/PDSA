#inputs are L&P 
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
    return sorted(val)[0]
