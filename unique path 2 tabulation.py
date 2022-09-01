class Solution:
    def uniquePathsWithObstacles(self, obs: List[List[int]]) -> int:
        dp=[[0 for _ in range(len(obs[0]))] for j in range(len(obs))]
        dp[0][0]=1
        for i in range(len(obs)):
            for j in range(len(obs[0])):
                if obs[i][j]==1:
                    dp[i][j]=0
                elif i==0 and j==0:
                    dp[i][j]=1
                else:
                    up=dp[i-1][j] if i>0 else 0
                    left=dp[i][j-1] if j>0 else 0
                    dp[i][j]=up+left

        return dp[len(obs)-1][len(obs[0])-1]