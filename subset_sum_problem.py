def subset_sum(li,n,w):
    for i in range(n+1):
        res=[]
        for j in range(w+1):
            res.append(False)
        t.append(res)
    for i in range(n+1):        
        for j in range(w+1):
            if i==0:
                t[i][j]=False
            if j==0:
                t[i][j]=True
    for i in range(1,n+1):
        for j in range(1,w+1):
            if li[i-1]<=j:
                t[i][j]=t[i-1][j-li[i-1]] or t[i-1][j]
            else:
                t[i-1][j]
    return t[n][w]
li = [1,5,11,7]
t=[]
n=4
w=7


#equal sum problem
if sum(li)%2==0:
    print(subset_sum(li,n,sum(li)//2))
else:
    print(False)

