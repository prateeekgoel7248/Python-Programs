def subsetSumToK(n, k, arr):
    # Write your code here
    # Return a boolean variable 'True' or 'False' denoting the answer
    #     def solve(ind,target,dp):
    #         if target==0:
    #             return True
    #         if ind==0:
    #             return arr[ind]==target
    #         if dp[ind][target]!=-1:
    #             return dp[ind][target]
    #         take=False
    #         if arr[ind]<=target:
    #             take = solve(ind-1,target-arr[ind],dp)
    #         ntake = solve(ind-1,target,dp)
    #         dp[ind][target]=take or ntake
    #         return dp[ind][target]
    #     dp=[[False]*(k+1)]*(n)
    prev = [False] * (k + 1)
    cur = [False] * (k + 1)
    #     return solve(n-1,k,dp)
    prev[0] = cur[0] = True
    if arr[0] <= k: prev[arr[0]] = True

    #     dp[0][k]=True
    for ind in range(1, n):
        for target in range(1, k + 1):
            take = False
            if arr[ind] <= target:
                take = prev[target - arr[ind]]
            ntake = prev[target]
            cur[target] = take or ntake
        prev = cur[:]
    return prev[k]
