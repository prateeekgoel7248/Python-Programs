class Solution(object):
    def subarraySum(self, nums, k):
        d=defaultdict(int)
        d[0]=1
        s=0
        cnt=0
        for i in nums:
            s+=i
            if s-k in d:
                # it is telling us that in the array there is a sum of array which is s-k 
                #so we have s-k and s so we have s-(s-k)= s-s+k = k so we have k also.
                cnt+=d[s-k]
                
            d[s]=d[s]+1
        return cnt
    
"""
    Just wanted to share a clear explanation that helped me.

First of all, the basic idea behind this code is that, whenever sums has increased by a value of k, we've found a subarray of sums=k.
I'll also explain why we need to initialise 0 in the hashmap.
Example: Let's say our elements are [1,2,1,3] and k = 3.
and our corresponding running sums = [1,3,4,7]
Now, if you notice the running sums array, from 1->4, there is increase of k and from 4->7, there is an increase of k. So, we've found 2 subarrays of sums=k.

But, if you look at the original array, there are 3 subarrays of sums==k. Now, you'll understand why 0 comes in the picture.

In the above example, 4-1=k and 7-4=k. Hence, we concluded that there are 2 subarrays.
However, if sums==k, it should've been 3-0=k. But 0 is not present in the array. To account for this case, we include the 0.
Now the modified sums array will look like [0,1,3,4,7]. Now, try to see for the increase of k.

0->3
1->4
4->7
Hence, 3 sub arrays of sums=k
"""
            
                
        