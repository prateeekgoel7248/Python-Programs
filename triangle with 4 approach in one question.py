class Solution(object):
    def solve(self,i,j,triangle,dp):
        if i>=len(triangle) or j>= len(triangle[-1]):
            return 0
        if dp[i][j]!=-1:
            return dp[i][j]
        dp[i][j]= triangle[i][j]+min(self.solve(i+1,j,triangle,dp),self.solve(i+1,j+1,triangle,dp))
        return dp[i][j]
    
    def minimumTotal(self, triangle):
        # dp=[[0 for _ in range(len(triangle[-1])+1)] for i in range(len(triangle)+1)]
        cur=[0 for _ in range(len(triangle)+1)]
        # post = [0 for _ in range(len(triangle)+1)]
        for i in range(len(triangle)-1,-1,-1):
            for j in range(len(triangle[i])):
                cur[j]= triangle[i][j]+min(cur[j],cur[j+1])
            # post = deepcopy(cur)
        return cur[0]
                
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        