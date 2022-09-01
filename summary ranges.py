class Solution(object):
    def summaryRanges(self, nums):
        
# def summaryRanges(self, nums):
        ranges = []
        for n in nums:
            if not ranges or n > ranges[-1][-1] + 1:
                ranges += [],
            ranges[-1][1:] = n,
            if n==0:
                print(ranges)
        print(ranges)
        return ['->'.join(map(str, r)) for r in ranges]
        