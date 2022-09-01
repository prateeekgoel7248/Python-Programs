class Solution(object):
    def minimumTotal(self, tri):
        # tri = triangle
        m = len(tri)
        dp = tri[-1]
        for i in range(m-1)[::-1]:
            # print(i)
            for j in range(len(tri[i])):
                dp[j] = tri[i][j] + min(dp[j], dp[j+1])

        return dp[0] 