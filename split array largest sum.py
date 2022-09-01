class Solution(object):
    def helper(self, nums, m):
#it is used to get that how many division of the array should be done to make it lesser or equal to mid
        count=0
        tempsum=0
        for i in range(len(nums)):
            if tempsum+nums[i] <=m:
                tempsum+=nums[i]
            else:
                count+=1
                tempsum=nums[i]
        count+=1
        return count
    def splitArray(self, nums, m):
        l, r = max(nums), sum(nums)
        mid=0
        ans=0
        while l <= r:
            mid = (l+r)//2
            count= self.helper(nums,mid)
            if count<=m:
                r=mid-1
                ans=mid
            else:
                l=mid+1
        #Just an simple approach to find the largest sum                  
        return ans
        """
        :type nums: List[int]
        :type m: int
        :rtype: int
        """
        