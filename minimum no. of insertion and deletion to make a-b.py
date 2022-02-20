def minOperations(self, s1, s2):
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
        return t[i][j]
    lcs_sol = lcs(s1,s2,len(s1),len(s2))
    ins = len(s1)-lcs_sol
    dele = len(s2)-lcs_sol
    
