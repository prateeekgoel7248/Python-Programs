class Solution(object):
    def subarraysWithKDistinct(self, nums, k):
        i=0
        j=0
        from collections import Counter
        d=Counter(nums)
        di=Counter()
        count=0
        ans1=ans2=0
        while j<len(nums):
            di[nums[j]]+=1
            while len(di)>=k:
                if nums[i] in di:
                    di[nums[i]]-=1
                    if di[nums[i]]==0:
                        di.pop(nums[i])
                i+=1
            ans1+=j-i+1
            j+=1
        di=Counter()
        i=0
        j=0
        while j<len(nums):
            di[nums[j]]+=1
            while len(di)>k:
                if nums[i] in di:
                    di[nums[i]]-=1
                    if di[nums[i]]==0:
                        di.pop(nums[i])
                i+=1
            
            ans2+=j-i+1
            j+=1
        print(ans1,ans2)
        return ans2-ans1
            
#         while j<len(nums):
#             if nums[j] in di:
#                 di[nums[j]]+=1
#             else:
#                 di[nums]=1
#             if len(di)<k:
#                 j+=1
#             elif len(di)==k:
#                 count+=1
#                 while len(di)==k:
#                     if nums[i] in di:
#                         di[nums[i]]-=1
#                         if di[nums[i]]==0:
#                             di.pop(nums[i])
                            
                        
            
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        