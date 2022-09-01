class Solution:
    # @param A : string
    # @param B : list of strings
    # @return an integer
    def wordBreak(self, s, wordDict):
        n = len(s)
        dp = [0 for i in range(n+1)]
        dp[n] = 1
        for i in range(n-1,-1,-1):
            for w in wordDict:
                if (i+len(w))<=len(s) and s[i:i+len(w)] == w:
                    dp[i]=dp[i+len(w)]
                if dp[i]:
                    break
        return dp[0]