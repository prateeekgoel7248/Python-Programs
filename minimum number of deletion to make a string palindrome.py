def minDeletions(self, Str, n):
    def lcs(x,y,m,n):
        t=[]
        
        for i in range(m+1):
            res=[]
            for j in range(n+1):
                res.append(-1)
            t.append(res)
        for i in range(m+1):
            t[i][0]=0
        for j in range(n+1):
            t[0][j]=0
            # for j in range(n+1):
            #     if i==0 or j==0:
            #         t[i][j]=0
        for i in range(1,m+1):
            for j in range(1,n+1):
                if x[i-1]==y[j-1]:
                    t[i][j]=1+t[i-1][j-1]
                else:
                    t[i][j]=max(t[i-1][j],t[i][j-1])
        return t[i][j]
    rev_str = Str[::-1]
    return n-lcs(Str,rev_str,n,n)
