class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        start=0
        end=len(A)-1
        res=0
        while start<=end:
            mid=start+(end-start)//2
            if A[mid]<=B:
                res=mid+1
                start=mid+1
            # elif A[mid]<B:
            #     res+=1
            #     start=mid+1
            else:
                end=mid-1
        return res
