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
        dp=[[-1 for _ in range(n)] for j in range(m)]
        return f(m-1,n-1,dp)