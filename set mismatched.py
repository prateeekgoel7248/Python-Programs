class Solution(object):
    def findErrorNums(self, nums):
                # Count for each element in nums
        from collections import Counter
        hashmap = Counter(nums)
        for num in range(1, len(nums)+1):
            # if number not present in hashpmap, that's the missing number
            if num not in hashmap:
                return (hashmap.most_common(1)[0][0], num)
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        