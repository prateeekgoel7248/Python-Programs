def coin_change(wt,n,w):
    for i in range(n+1):
        res=[]
        for j in range(w+1):
            res.append(-1)
        t.append(res)
    for i in range(n+1):
        #res=[]
        for j in range(w+1):
            if i==0:
                t[i][j]=0
            if j==0:
                t[i][j]=1
            #res.append(-1)
        #t.append(res)
        
    for i in range(1,n+1):
        for j in range(1,w+1):
            if wt[i-1]<=j:
                t[i][j]=t[i-1][j]+t[i][j-wt[i-1]]
            else:
                t[i][j]=t[i-1][j]
    return t[n][w]



coin=[1,2,3]
summ=5
t=[]
n=3
print(coin_change(coin,n,summ))
