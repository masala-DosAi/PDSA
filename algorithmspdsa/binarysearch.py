def binary(v,l):
    if l==[]:
        return False
    m=len(l)//2

    if v==l[m]:
        return True
    
    if v<l[m]:
        return binary(v,l[:m])
    
    if v>l[m]:
        return binary(v,l[m+1:])
    

inp=[1,2,3,4,5,6,7,8,9,10,15,20,25,26,28,30]

print(binary(24,inp))


#time complexity O(logn) in sorted list
#time complexity O(n) in unsorted list
