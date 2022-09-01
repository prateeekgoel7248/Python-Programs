import sys
def unboundedKnapsack(n, w, profit, weight):
    def solve(ind,val,wt,w):
        if ind==0:
            return (w//wt[0])*val[0]
        if dp[ind][w]!=-1:
            return dp[ind][w]
        notTake = solve(ind-1,val,wt,w)
        take = - sys.maxsize
        if wt[ind]<=w:
            take = val[ind]+solve(ind,val,wt,w-wt[ind])
        dp[ind][w]=max(take,notTake)
        return dp[ind][w]
    # Write Your code here.
    dp=[[-1 for _ in range(w+1)] for i in range(n+1)]
    return solve(n-1,profit,weight,w)