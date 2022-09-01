class Solution(object):
    def mySqrt(self, x):
        if (x == 0):
            return 0
        if (x == 1):
            return 1
        low = 1
        high = x
        while(low <= high):  
            mid = (low + high)//2
            
            if(mid == (x/mid)):
                return mid
            elif(mid <= (x/mid)):   # mid * mid <= x     therefore mid <= (x/mid)
                low = mid + 1
            else:
                high = mid - 1
        return high
        """
        :type x: int
        :rtype: int
        """
        