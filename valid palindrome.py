class Solution(object):
    def isPalindrome(self,string,low,high):
        while low<high:
            if string[low]!=string[high]:
                return False
            low+=1
            high-=1
        return True
    def validPalindrome(self, s):
        low=0
        high=len(s)-1
        while low<=high:
            if s[low]!=s[high]:
                return self.isPalindrome(s,low,high-1) or self.isPalindrome(s,low+1,high)
            low+=1
            high-=1
        return True
        # start=0
        # end=len(s)-1
        # count=0
        # while start<end:
        #     if s[start]==s[end]:
        #         start+=1
        #         end-=1
        #     elif s[start+1]==s[end]:
        #         count+=1
        #         start+=1
        #     elif s[start]==s[end-1]:
        #         count+=1
        #         end-=1
        #     else:
        #         start+=1
        #         end-=1
        #         count+=2
        # if count<=1:
        #     return True
        # else:
        #     return False
            
        """
        :type s: str
        :rtype: bool
        """
        