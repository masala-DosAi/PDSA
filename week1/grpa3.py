def odd_one(L):
    d=[]
    for x in L:
        if type(x)==int:
            d.append('int')
        if type(x)==float:
            d.append('float')
        if type(x)==str:
            d.append('str')
        if type(x)==bool:
            d.append('bool')
        if type(x)==list:
            d.append('list')
        if type(x)==tuple:
            d.append('tuple')
        if type(x)==dict:
            d.append('dict')
    D=sorted(d)
    if D[0]!=D[1]:
        return D[0]
    else:
        return D[-1]
