#User function Template for python3
import sys
class Solution:
    def palindromicPartition(self, string):
        if len(string)==0 or len(string)==1:
            return 0
        # code here
        def isPalindrome(st,i,j):
            # i
            if i>=j:
                return True
            while i<j:
                if st[i]!=st[j]:
                    return False
                i+=1
                j-=1
            return True
        def solve(s,i,j):
            # if i==j:
            #     return True
            if i>=j:
                return 0
            if t[i][j]!=-1:
                return t[i][j]
            if isPalindrome(s,i,j):
                return 0
            mn = sys.maxsize
            for k in range(i,j):
                if(isPalindrome(s,i,k)):
                    left=0
                    right=0
                    if t[i][k]!=-1:
                        left = t[i][k]
                    else:
                        left = solve(s,i,k)
                        t[i][k]= left
                    if t[k+1][j]!=-1:
                        right=t[k+1][j]
                        temp = left+right+1
                    else:
                        right = solve(s,k+1,j)
                        
                        temp = left+right+1
                        t[k+1][j]=right
                    if mn>temp:
                        mn=temp
            t[i][j]=mn
            return mn
            
        t=[]
        for i in range(len(string)+1):
            res=[]
            for j in range(len(string)+1):
                res.append(-1)
            t.append(res)
        return solve(string,0,len(string)-1)

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range (t):
        string = input()
        
        ob = Solution()
        print(ob.palindromicPartition(string))
# } Driver Code Ends
