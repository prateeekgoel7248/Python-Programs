class Solution:
	# @param A : integer
	# @return an integer
	def climbStairs(self, A):
        # return 2
        dp=[-1 for i in range(A)]
        if A==0:
            return 1
        dp[0]=1
        if A==1:
            return dp[0]
        dp[1]=2
        for i in range(2,A):
            dp[i]=dp[i-1]+dp[i-2]
        return dp[(A)-1]
        