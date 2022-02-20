class Solution(object):
    def letterCombinations(self, digits):
        
        
        if not digits or len(digits) == 0:
            return []
        dict1 = {'2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
        if len(digits) == 1:
            return list(dict1[digits[0]])
        now = dict1[digits[0]]
        digits = digits[1:]
        after = self.letterCombinations(digits)
        ans = []
        for x in now:
            for y in after:
                ans.append(x+y)
        return ans        
        
        """
        :type digits: str
        :rtype: List[str]
        """
        