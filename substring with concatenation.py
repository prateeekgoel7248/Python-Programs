class Solution:
    # @param A : string
    # @param B : tuple of strings
    # @return a list of integers
    def findSubstring(self, s, words):
        l=len(words[0])
        noOfWords=len(words)
        result=[]
        from collections import defaultdict,Counter
        
        d=defaultdict(int)
        d=Counter(words)
        for ind in range(len(s)-(noOfWords*l)+1):
            used = defaultdict(int)
            for c in range(ind,ind+(noOfWords*l),l):
                cur = s[c:c+l]
                if d[cur]==0:
                    break
                used[cur]+=1      
                if used[cur]>d[cur]:
                    break
            # print(used,d)
            if used == d:
                result.append(ind)
        return result