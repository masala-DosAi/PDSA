def quicksort(L,l,r):
    if r-1<=1:
        return L
    pivot,lower,upper=l=L[1],l+1
    