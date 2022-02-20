#User function Template for python3
import sys
class Solution:
    def matrixMultiplication(self, N, arr):
        def mat(arr,i,j):
            if i>=j:
                return 0
            if t[i][j]!=-1:
                return t[i][j]
            mn = sys.maxsize
            for k in range(i,j):
                temp = mat(arr,i,k)+mat(arr,k+1,j)+arr[i-1]*arr[k]*arr[j]
                
                if mn>temp:
                    mn=temp
            t[i][j]=mn
            return mn
        
        
        
        t=[]
        for i in range(N+1):
            res=[]
            
            for j in range(N+1):
                res.append(-1)
            t.append(res)
        return mat(arr,1,len(arr)-1)
                
        
        # code here

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        arr = input().split()
        for i in range(N):
            arr[i] = int(arr[i])
        
        ob = Solution()
        print(ob.matrixMultiplication(N, arr))
# } Driver Code Ends
