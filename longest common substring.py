def lcs(x,y,m,n):
    t=[]
    max_sub=0
    for i in range(m+1):
        res=[]
        for j in range(n+1):
            res.append(-1)
        t.append(res)
    for i in range(m+1):
        for j in range(n+1):
            if i==0 or j==0:
                t[i][j]=0
    for i in range(m+1):
        for j in range(n+1):
            if x[i-1]==y[j-1]:
                t[i][j]=1+t[i-1][j-1]
                max_sub=max(max_sub,t[i][j])
            else:
                t[i][j]=0
    return max_sub
x="abcefgdqwer"
y="abcklwdfgdqwek"
print(lcs(x,y,len(x),len(y)))
