class Solution(object):
    def totalSteps(self, nums):
        ans = 0
        nums.reverse()
        # print(nums)
        lst = [[nums[0], 0]]
        for i in range(1, len(nums)):
            cnt = 0
            while lst and lst[-1][0] < nums[i]:
                # print(lst[-1],nums[i])
                cnt = max(cnt + 1, lst[-1][1])
                lst.pop()
            lst.append([nums[i], cnt])
            ans = max(ans, cnt)
        # print(lst)
        return ans
            
        """
        :type nums: List[int]
        :rtype: int
        """
        