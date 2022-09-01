#User function Template for python3
class Solution:
    def solve(self,ind,arr,s,ans):
        if ind>=len(arr):
            ans.append(s)
            return
        self.solve(ind+1,arr,s,ans)
        self.solve(ind+1,arr,s+arr[ind],ans)
	def subsetSums(self, arr, N):
	    ans=[]
	    self.solve(0,arr,0,ans)
	    return ans
		# code here

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T=int(input())
    for i in range(T):
        N = int(input())
        arr = [int(x) for x in input().split()]
        ob = Solution()
        ans = ob.subsetSums(arr, N)
        ans.sort()
        for x in ans:
            print(x,end=" ")
        print("")

# } Driver Code Ends