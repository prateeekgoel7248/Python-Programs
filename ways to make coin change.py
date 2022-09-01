from sys import stdin,setrecursionlimit
setrecursionlimit(10**7)
def countWaysToMakeChange(arr, value) :
    
    def solve(ind,target):
        if ind==0:
            return target%arr[0]==0
        if dp[ind][target]!=-1:
            return dp[ind][target]
        notTake = solve(ind-1,target)
        take=0
        if arr[ind]<=target:
            take = solve(ind,target-arr[ind])
        dp[ind][target]=notTake+take
        return dp[ind][target]
    dp=[[-1 for _ in range(value+1)] for i in range(len(arr)+1)]
	# Your code goes here
    return solve(len(arr)-1,value)































#taking inpit using fast I/O
def takeInput() :
    numDenominations = int(input())

    denominations = list(map(int, stdin.readline().strip().split(" ")))

    value = int(input())
    return denominations, numDenominations, value


#main
denominations, numDenomination, value = takeInput()
print((countWaysToMakeChange(denominations, value)))