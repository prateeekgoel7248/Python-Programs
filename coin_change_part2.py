#User function Template for python3
import sys
class Solution:
	def minCoins(self, coins, M, V):
	    
	    t=[]
	    for i in range(M+1):
	        res=[]
	        for j in range(V+1):
	            res.append(-1)
	        t.append(res)
	    for i in range(M+1):
	        
    	    for j in range(V+1):
    	        
    	        
    	        if j==0:
    	            
    	            t[i][j]=0
    	        if i==0:
    	            
    	            t[i][j]=sys.maxsize-1
    	 
	   # i=2
	   # if i<M+1:
	       # for j in range(1,V+1):
	       #     if j%coins[0]==0:
	       #         t[1][j]=j//coins[0]
	       #     else:
	       #         t[1][j]=sys.maxsize-1
	                
	    for i in range(1,M+1):
	        
	        for j in range(1,V+1):
	            
	            if coins[i-1]<=j:
	                t[i][j]=min(t[i][j-coins[i-1]]+1,t[i-1][j])
	                
	            else:
	                
	                t[i][j]=t[i-1][j]
	                
	    if t[M][V] > V:
	        return -1
	    else:
	        return t[M][V]
	               
	                
		# code here

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		v,m = input().split()
		v,m = int(v), int(m)
		coins = [int(x) for x in input().split()]
		ob = Solution()
		ans = ob.minCoins(coins,m,v)
		print(ans)

# } Driver Code Ends
