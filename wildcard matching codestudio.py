class Solution(object):
    def isMatch(self, s, p):
        n=len(s)
        m=len(p)
        dp=[[False for _ in range(len(p)+1)] for i in range(len(s)+1)]
        # def f(n,m):
        #     if n<0 and m<0:
        #         return True
        #     if n>=0 and m<0:
        #         return False
        #     if n<0 and m>=0:
        #         for i in range(m+1):
        #             if p[i]!='*':
        #                 return False
        #         return True
        #     if dp[n][m]!=-1:
        #         return dp[n][m]
        #     ans = False
        #     if (s[n]==p[m] or p[m]=='?'):
        #         ans = f(n-1,m-1)
        #     elif p[m]=="*":
        #         ans = f(n,m-1) or f(n-1,m)
        #     dp[n][m]=ans
        #     return ans
        # return f(len(s)-1,len(p)-1)
        dp[0][0]=True
        for j in range(1, len(p)+1):
            if p[j-1] != '*':
                break
            dp[0][j] = True
                
        for i in range(1,n+1):
            for j in range(1,m+1):
                # ans=False
                if s[i-1]==p[j-1] or p[j-1]=="?":
                    dp[i][j]=dp[i-1][j-1]
                elif p[j-1]=='*':
                    dp[i][j]=dp[i-1][j] or dp[i][j-1]
                
        return dp[n][m]
    
    
    
#         dp = [[False for _ in range(len(p)+1)] for i in range(len(s)+1)]
#         dp[0][0] = True
#         for j in range(1, len(p)+1):
#             if p[j-1] != '*':
#                 break
#             dp[0][j] = True
                
#         for i in range(1, len(s)+1):
#             for j in range(1, len(p)+1):
#                 if p[j-1] in {s[i-1], '?'}:
#                     dp[i][j] = dp[i-1][j-1]
#                 elif p[j-1] == '*':
#                     dp[i][j] = dp[i-1][j] or dp[i][j-1]
#         return dp[-1][-1]
        
