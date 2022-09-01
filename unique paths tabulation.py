class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        def f(i,j,dp):
            if i==0 and j==0:
                return 1
            if i<0 or j<0:
                return 0
            if dp[i][j]!=-1:
                return dp[i][j]
            up=f(i-1,j,dp)
            left=f(i,j-1,dp)
            dp[i][j]=up+left
            return dp[i][j]
        dp=[[0 for _ in range(n)] for j in range(m)]
        prev=[0 for _ in range(n)]
        curr=[0 for _ in range(n)]
        # return f(m-1,n-1,dp)
        dp[0][0]=1
        for i in range(0,m):
            for j in range(0,n):
                if i==0 and j==0:
                    dp[0][0]=1
                else:
                    up=dp[i-1][j]
                    left=dp[i][j-1]
                    dp[i][j]=up+left
        return dp[m-1][n-1]
                