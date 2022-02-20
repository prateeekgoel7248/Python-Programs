def lcs(x,y,m,n):
    t=[]
    
    for i in range(m+1):
        res=[]
        for j in range(n+1):
            res.append(-1)
        t.append(res)
    for i in range(m+1):
        for j in range(n+1):
            if i==0 or j==0:
                t[i][j]=0

            elif x[i-1]==y[j-1]:
                t[i][j]=1+t[i-1][j-1]
            else:
                t[i][j]=max(t[i-1][j],t[i][j-1])
    result=""
    i=m
    j=n
    while i>0 and j>0:
        if x[i-1]==y[j-1]:
            result+=x[i-1]
            i-=1
            j-=1
        else:
            if t[i-1][j]>t[i][j-1]:
                result+=x[i-1]
                i-=1
            else:
                result+=y[j-1]
                j-=1
    print(result)
    for k in t:
        print(k)
    while i>0:
        result+=x[i-1]
        i-=1
    while j>0:
        result+=y[j-1]
        j-=1
    return result[::-1]
    
        
x="abcdaf"
y="acbcf"

print(lcs(x,y,len(x),len(y)))
      
