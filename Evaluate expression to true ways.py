#User function Template for python3

class Solution:
    def countWays(self, N, S):
        def solve(s,i,j,istrue):
            if i>j:
                return 0
            
            if i==j:
                if istrue==True:
                    return 1 if s[i]=='T' else 0
                else:
                    return 1 if s[i]=='F' else 0
            if t[istrue][i][j]!=-1:
                return t[istrue][i][j]
            ans=0
            for k in range(i+1,j,2):
                lt=solve(s,i,k-1,1)
                lf=solve(s,i,k-1,0)
                rt=solve(s,k+1,j,1)
                rf=solve(s,k+1,j,0)
                # print(lt,lf,rt,rt)
                
                if s[k]=='|':
                    if istrue==1:
                        ans+=lt*rt+lf*rt+lt*rf
                    else:
                        ans+=lf*rf
                elif s[k]=='&':
                    if istrue==1:
                        ans+=lt*rt
                    else:
                        ans+=lf*rf+lf*rt+lt*rf
                elif s[k]=='^':
                    if istrue==1:
                        ans+=lt*rf+lf*rt
                    else:
                        ans+=lf*rf+lt*rt
            t[istrue][i][j]=ans%mod
            return ans%mod
            
        t=[]
        mod=1003
        for i in range(2):
            t.append([])
            for j in range(N+1):
                t[i].append([])
                for k in range(N+1):
                    t[i][j].append(-1)
                    
        return solve(S,0,N-1,True)        
        # code here

#{ 
#  Driver Code Starts
#Initial Template for Python 3

import sys
sys.setrecursionlimit(10**6)

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        S = input()
        
        ob = Solution()
        print(ob.countWays(N, S))
# } Driver Code Ends
