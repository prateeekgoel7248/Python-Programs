class Solution(object):
    def isMatch(self, s, p):
        dp=[[-1 for _ in range(len(p)+1)] for i in range(len(s)+1)]
        def f(n,m):
            if m==len(p):
                return n==len(s)
            if  n==len(s) and m==len(p):
                return True
            if n==len(s):
                for i in range(m,len(p)):
                    if p[i]!="*":
                        return False
                return True
            if dp[n][m]!=-1:
                return dp[n][m]
            ans = False
            # print(n,m,s[n],p[m])
            if p[m]=="*":
                ans = f(n,m+1) or f(n+1,m)
                # ans = ans or f(n,m-1)
            elif s[n]==p[m] or p[m]=='?':
                ans = ans or f(n+1,m+1)
            dp[n][m]=ans
            return ans
        return f(0,0)
    
 