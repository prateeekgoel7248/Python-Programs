class Solution(object):
    def wordBreak(self, s, wordDict):
        n = len(s)
        dp = [False for i in range(n+1)]
        dp[0] = True
        for i in range(1,n+1):
            for w in wordDict:
                if dp[i-len(w)] and s[i-len(w):i]==w:
                    dp[i]=True
        print(dp)
        return dp[-1]
        