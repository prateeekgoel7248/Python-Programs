class Solution(object):
    def threeSumClosest(self, nums, target):
        nums=sorted(nums)
        import sys
        mx=sys.maxsize
        # ans=0
        for i in range(len(nums)-2):
            j=i+1
            k=len(nums)-1
            while j<k:
                s=nums[i]+nums[j]+nums[k]
                if s<target:
                    j=j+1
                elif s>target:
                    k=k-1
                else:
                    k=k-1
                    j=j+1
                    
                if abs(target-s)<mx:
                    ans=s
                    mx=abs(target-s)
        return ans
        #     ans=0

        # nums= sorted(nums)

#         value =sys.maxsize

#         for i in range(len(nums)-2):
#             j=i+1
#             k=len(nums)-1

#             while j<k:
#                 s=nums[i]+nums[j]+nums[k]

#                 if s<target:
#                     j=j+1
#                 elif s>target:
#                     k=k-1
#                 else:
#                     k=k-1
#                     j=j+1

#                 if abs(target-s)<value:
#                     ans=s
#                     value=abs(target-s)

#         return ans
        # while j<len(nums):
        #     s+=nums[j]
    
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        