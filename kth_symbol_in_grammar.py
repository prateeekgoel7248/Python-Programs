def comp(li):
    li=[int(x) for x in str(li)]
    resu=[]
    for i in li:
        if i==0:
            resu.append(1)
        else:
            resu.append(0)
    res_str =""
    for i in resu:
        res_str+=str(i)
    return int(res_str)
def solve(n,k):
    if n==1:
        #res.append(0)
        return 0
    #mid=int(k/2.0+1)
    mid=pow(2,n-1)//2
    
        
    if k<=mid:
        return solve(n-1,k)
    else:
        return comp(solve(n-1,k-mid))
    
        

n=1
k=1
res=[]
print(solve(n,k))
#print(res)

"""
def pattern(n,k,res):
    if n==1:
        return 0
    mid=(2**(n-1))//2
    if k<=mid:
        return pattern(n-1,k-1,res)
        
    else:
        return ~(pattern(n-1,k-mid,res))
"""
