class Solution(object):
    def smallestNumber(self, num):
        plus = num >= 0
        if not plus: num = -num
        
        nums = sorted(str(num))
        if plus:
            for i, dig in enumerate(nums):
                if dig != '0': break
            nums = [dig] + nums[:i] + nums[i+1:]
        else:
            nums = nums[::-1]
            
        num = int("".join(nums))
        if not plus: num = -num
            
        return num
            
            
            
        