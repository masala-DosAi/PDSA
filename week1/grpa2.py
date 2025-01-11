def is_prime(n):
    l=[]
    for x in range(1,n+1):
        if n%x==0:
            l.append(x)
    return (len(l)==2)
    


def Goldbach(n):
    p=[]
    t=[]
    for x in range(n+1):
        if is_prime(x):
            t.append(x)
    for y in t:
        for z in t:
            if y<=z and y+z==n:
                p.append((y,z))
    return p
