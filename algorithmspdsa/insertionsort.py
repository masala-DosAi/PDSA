def insertionsort(l):
    for i in range(1,len(l)):
        j=i
        while l[j-1]>l[j] and j>0:
            l[j-1],l[j]=l[j],l[j-1]
            j-=1
    return l
test=[1,5,4,8,9,7,6,2,5,4,6,8]
print(insertionsort(test))

#tiem complexity O(n)