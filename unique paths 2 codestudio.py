def mazeObstacles(n, m, mat):
    # Write your code here.
    def solve(i,j,dp):
        if i<0 and j<0:
            return 0
        if i>0 and j>0 and mat[i][j]==-1:
            return 0
        if i==0 and j==0:
            return 1
        
        if dp[i][j]!=-1:
            return dp[i][j]
        dp[i][j]=solve(i-1,j,dp)+solve(i,j-1,dp)
        return dp[i][j]%(10**9+7)
    dp=[[0 for _ in range(m)] for i in range(n)]
#     return solve(n-1,m-1,dp)
    for i in range(n):
        for j in range(m):
            if mat[i][j]==-1:
                dp[i][j]=0
            elif i==0 and j==0:
                dp[i][j]=1
            else:
                left=0
                up=0
                if i>0:
                    left = dp[i-1][j]
                if j>0:
                    up = dp[i][j-1]
                dp[i][j]=(up+left)%(10**9+7)
    return dp[n-1][m-1]