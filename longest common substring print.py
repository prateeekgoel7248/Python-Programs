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
    result=""
    print(max_sub)
    i=m
    j=n
    while t[i][j]==0:
        i=i-1
        j-=1
    print(i,j)
    i+=1
    j+=1
    while i>0 and j>0:
        if x[i-1]==y[j-1]:
            
            result+=x[i-1]
            i=i-1
            j=j-1
        else:
            i=0
            j=0
       #not working code 
        
    return result[::-1]
x="abcefgdqwerasdfg"
y="abcklwdfgdqwek"
print(lcs(x,y,len(x),len(y)))
