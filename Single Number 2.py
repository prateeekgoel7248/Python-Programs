#Approach 1- Usign Bit Counting

class Solution(object):
    def singleNumber(self, nums):
        print(bin(-4))
        n=len(nums)
        ans=0
        shift=1
        for i in range(32):
            count=0
            for ele in nums:
                if ele & shift:
                    count+=1
            if count%3!=0 and i==31:
                #as we all know that a number which is negative have a set bit of last bit as 1 for the minus point 
                #so we will check that the number is negative or not
                #take example of [4,4,4,-4] so -4 32th bit will be as 1 for the representation of minus sign.
                ans-=shift
            elif count%3!=0:
                ans+=shift
            shift*=2
        return ans
                

#Approach 2 - Bit Manipulation

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ones=0
        twos=0
        for i in nums:
            ones=(ones^i)&(~twos)
            twos=(twos^i)&(~ones)
        return ones
    #it is not very intuitive approach.


