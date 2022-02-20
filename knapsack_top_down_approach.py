n=7
w=3
wt=[1,2,3,4,5,6,7]
val=[2,3,4,5,6,7,8]
t=[]
for i in range(n+1):
    res=[]
    for j in range(w+1):
        res.append(-1)
    t.append(res)
for i in range(n+1):
    #res=[]
    for j in range(w+1):
        if i==0 or j==0:
            t[i][j]=0
for i in range(1,n+1):
    for j in range(1,w+1):
        if wt[i-1]<=j:            
            t[i][j]=max((val[i-1]+t[i-1][j-wt[i-1]]),t[i-1][j])
            
        else:
            
            t[i][j]=t[i-1][j]
print(t[n][w])
