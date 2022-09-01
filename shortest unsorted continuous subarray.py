class Solution(object):
    def findUnsortedSubarray(self, nums):
        n=len(nums)
        mx=0
        mn=n-1
        l=0
        l=0
        r=n-1
        for i in range(n):
            if nums[i]>nums[mx]:
                mx=i
            elif nums[i]<nums[mx]:
                l=i
            if nums[n-i-1]<nums[mn]:
                mn=n-i-1
            elif nums[n-i-1]>nums[mn]:
                r=n-i-1
        if r>=l:
            return 0
        return l-r+1
        """
        :type nums: List[int]
        :rtype: int
        """
        