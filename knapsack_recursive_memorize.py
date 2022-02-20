def knapsack(wt,val,w,n):
    if n==0 or w==0:
        return 0
    if t[n][w]!=-1:
        return t[n][w]
    
    if wt[n-1]<=w:
        t[n][w]= max(val[n-1]+knapsack(wt,val,w-wt[n-1],n-1),knapsack(wt,val,w,n-1))
        return t[n][w]
    elif wt[n-1]>w:
        t[n][w]=knapsack(wt,val,w,n-1)
        return t[n][w]

n=7
w=1
wt=[1,2,3,4,5,6,7]
val=[2,3,4,5,6,7,8]
#w=5
#W=1
t=[]
for i in range(n+1):
    res=[]
    for j in range(w+1):
        res.append(-1)
    t.append(res)
print(t)
print(knapsack(wt,val,w,n))
print(t)
