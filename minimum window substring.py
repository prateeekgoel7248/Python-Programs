class Solution(object):
    def minWindow(self, s, t):
        if len(s)<len(t):
            return ""
        
        d=dict()
        i=0
        j=0
        from collections import Counter
        d=Counter(t)
        count = len(d)
        start=0
        import sys
        mn= (sys.maxsize)
        while j<len(s):
            if s[j] in d:
                d[s[j]]-=1
                if d[s[j]]==0:
                    count-=1
            if count>0:
                j+=1
            elif count==0:
                # if mn>j-i+1:
                #     mn=j-i+1
                #     start=i
                while count==0:
                    if s[i] in d:
                        d[s[i]]+=1
                        if d[s[i]]>0:
                            count+=1                   
                    i+=1
                if mn>j-i+2:
                    #we are taking j-i+2 because when the count increase there will be
                    #i which goes more one place.
                    #so for  the original start we have to goto j-i+2 to get the correct minimum length.
                    
                    mn=j-i+2
                    start=i
                j+=1
            # print(i,j)
        print(mn)
        print(i,j)
        print(start)
        if mn==sys.maxsize:
            return ""
        return (s[start-1:start-1+mn])
        # return "BANC"
            # else:
                
                
                
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        
