class Solution(object):
    def singleNumber(self, nums):
        xor=0
        for i in nums:
            xor^=i
#as we all know that the same number twice will give 0 so we get only the  xor of unique numbers here and we will get that there are some unique bits because both two single values are different.
        ans=[0,0]
        res=1
        while True:
            if xor & res:
                break
            res*=2
        for i in nums:
            if i&res:
                ans[0]^=i
            else:
                ans[1]^=i
        return ans