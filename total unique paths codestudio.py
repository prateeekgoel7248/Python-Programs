from os import *
from sys import *
from collections import *
from math import *

def uniquePaths(m, n):
	# Write your code here.
        def solve(i,j,dp):
            if i==0 and j==0:
                return 1
            if i<0 or j<0:
                return 0
            if dp[i][j]!=-1:
                return dp[i][j]
            left = solve(i-1,j,dp)
            right=solve(i,j-1,dp)
            dp[i][j]=left+right
            return dp[i][j]
        dp=[[0 for _ in range(n+1)] for i in range(m+1)]
        dp[0][0]=1
        prev=[0]*n
        curr=[0]*n
        for i in range(m):
            for j in range(n):
                if i==0 and j==0:
                    curr[j]=1
                else:
                    left=right=0
                    if i>0:
                        left = prev[j]
                    if j>0:
                        right=curr[j-1]
                    curr[j]=left+right
            prev = curr[:]
                
        
        return prev[n-1]