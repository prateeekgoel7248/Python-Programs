#User function Template for python3

class Solution:
    def minTime (self, arr, n, k):
        def valid(m):
            count=1
            temp=m
            for i in arr:
                temp-=i
                if temp<0:
                    temp=m
                    temp-=i
                    count+=1
            return count<=k
                
                
        start=max(arr)
        end=sum(arr)
        res=-1
        while start<=end:
            mid = start+(end-start)//2
            if valid(mid):
                res=mid
                end=mid-1
            else:
                start=mid+1
        return res
        

#{ 
#  Driver Code Starts
#Initial Template for Python 3


if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        str = input().split()
        k = int(str[0])
        n = int(str[1])
        arr = input().split()
        for itr in range(n):
            arr[itr] = int(arr[itr])

        ob = Solution()
        print(ob.minTime(arr,n,k))
# } Driver Code Ends