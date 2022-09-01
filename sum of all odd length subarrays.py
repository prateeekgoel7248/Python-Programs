class Solution(object):
    def sumOddLengthSubarrays(self, A):
        res, n = 0, len(A)
        for i, a in enumerate(A):
            res += ((i + 1) * (n - i) + 1) / 2 * a
        return res
    #i+1 pointing to the left arrray and n-i pointing to the right array and for  odd we know that t+1//2 and a is the a[i]th element 
    
        # n = len(A)
        # res = 0
        # for l in range(1, n + 1, 2):
        #     for i in range(n - l + 1):
        #         res += sum(A[i:i + l])
        # return res
        
        # for i in range(len(arr)):
        #     for j in range(i,len(arr)):
        #         if len(arr[i:j+1])%2==1:
        #             s=s+sum(arr[i:j+1])
        # return s
        """
        :type arr: List[int]
        :rtype: int
        """
        