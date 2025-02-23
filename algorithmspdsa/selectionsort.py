def selectioinsort(l):
    n=len(l)
    if n<1:
        return l
    for i in range(n):
        mpos=i
        for j in range(i+1,n):
            if l[j]<l[mpos]:
                mpos=j
        l[i],l[mpos]=l[mpos],l[i]
    return l

test=[7,4,6,566,4,5,4,6,8,4,75,8,5,4,5,4,65,65,65,26,56,5,5,5,65,5,5,8,86,44]
print(selectioinsort(test))


#time complexity O(n^2)


