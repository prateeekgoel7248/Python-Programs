def shortestSupersequence(s: str, t: str) -> str:
	# Write your code here.

    dp=[[0 for _ in range(len(t)+1)] for i in range(len(s)+1)]
#     prev = [0 for _ in range(l+1)]
#     curr = prev[:]
    
    #     return solve(len(s)-1,len(t)-1)
    for ind1 in range(1,len(s)+1):
        for ind2 in range(1,len(t)+1):
            if s[ind1-1]==t[ind2-1]:
                dp[ind1][ind2]= 1+dp[ind1-1][ind2-1]
            else:
                dp[ind1][ind2] = max(dp[ind1-1][ind2],dp[ind1][ind2-1])
    ans=""
    i=len(s)
    j=len(t)
    while i>0 and j>0:
        if(s[i-1]==t[j-1]):
            i-=1
            j-=1
            ans+=s[i]
        elif dp[i-1][j]>dp[i][j-1]:
            ans+=s[i-1]
            i-=1
        else:
            ans+=t[j-1]
            j-=1
    while i>0:
        ans+=s[i-1]
        i-=1
    while j>0:
        ans+=t[j-1]
        j-=1
    return ans[::-1]

            