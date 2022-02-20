def subset_sum(li,n,w):
    t=[]
    su=(w+1)//2
    for i in range(n+1):
        res=[]
        for j in range(su+1):
            res.append(False)
        t.append(res)
    for i in range(n+1):
        for j in range(su+1):
            if i==0:
                t[i][j]=False
            if j==0:
                t[i][j]=True
    for i in range(1,n+1):
        for j in range(1,su+1):
            if li[i-1]<=j:
                
                t[i][j]=t[i-1][j] or t[i-1][j-li[i-1]]
            else:
                t[i][j]=t[i-1][j]
    mn=100000
    for i in range(su+1):
        if t[n][i]:
            mn=min(mn,sum(li)-2*i)
    return mn
arr=[1,6,15,5]
print(abs(subset_sum(arr,len(arr),sum(arr))))
