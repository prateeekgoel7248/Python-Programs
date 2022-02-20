class Solution(object):
    def countVowelSubstrings(self, word):
        from collections import Counter
        d=defaultdict(lambda: 0)
        vowel="aeiou"
        # i=0
        # left=0
        # pivot=0
        # count=len(d)
        result=0
        for i,char in enumerate(word):
            if char in vowel:
                d[char]+=1
                if word[i-1] not in vowel or i==0:
                    pivot=left=i
                while len(d)==5 and all(d.values()):
                    d[word[pivot]]-=1
                    pivot+=1
                result +=(pivot-left)
                    
            else:
                d.clear()
                left=pivot=i+1
        return result
                
                
        
        # ans=0
        # while j<len(word):
        #     if word[j] in d:
        #         d[word[j]]-=1
        #         if d[word[j]]==0:
        #             count-=1
        #     if j-i+1<k:
        #         j+=1
        #     elif j-i+1==k:
        #         if count==0:
        #             ans+=1
        #         if word[i] in d:
        #             d[word[i]]+=1
        #             if d[word[i]]==1:
        #                 count+=1
        #         i+=1
        #         j+=1
        # print(ans)
        # return ans
            
                
        """
        :type word: str
        :rtype: int
        """
        