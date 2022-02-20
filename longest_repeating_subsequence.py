def lcs(x,y,m,n):
    t=[]
    
    for i in range(m+1):
        res=[]
        for j in range(n+1):
            res.append(-1)
        t.append(res)
    for i in range(m):
        t[i][0]=0
    for j in range(n):
        t[0][j]=0
    for i in range(1,m+1):
        for j in range(1,n+1):
            #if i==0 or j==0:
                #t[i][j]=0
            if x[i-1]==y[j-1] and i!=j:
                t[i][j]=1+t[i-1][j-1]
            else:
                t[i][j]=max(t[i-1][j],t[i][j-1])
    for i in t:
        print(i)
    return t[m][n]
#x="jxyrnbvtfc"
x="AABEBCDD"
#y="abcklwd"
print(lcs(x,x,len(x),len(x)))
