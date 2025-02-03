def DishPrepareOrder(nums):
    z=[]
    d={}
    for x in nums:
        if x in d.keys():
            d[x][1]+=1
        else:
            d[x]=[x,1]
    return sorted(d,key=lambda x:(-d[x][1],d[x][0]),reverse=True)[::-1]
   