class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        def valid(s):
            count=1
            temp=s
            for i in nums:
                temp-=i
                if temp<0:
                    count+=1
                    temp=s
                    temp-=i
            return count<=m
        start=max(nums)
        end=sum(nums)
        # res=-1
        while start<=end:
            mid=start+(end-start)//2
            # print(mid)
            if valid(mid):
                end=mid-1
                # res=mid
            else:
                start=mid+1
        return start