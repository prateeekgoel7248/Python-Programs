class Solution(object):
    def isMatch(self, s, p):
        t=[]
        for i in range(len(s)+1):
            res=[]
            for j in range(len(p)+1):
                res.append(False)
            t.append(res)
        t[0][0]=True
        for i in range(2,len(p)+1):
            if p[i-1]=="*":
                t[0][i]=t[0][i-2]
        for i in range(1,len(s)+1):
            for j in range(1,len(p)+1):
                if s[i-1]==p[j-1] or p[j-1]=='.':
                    t[i][j]=t[i-1][j-1]
                elif p[j-1]=='*':
                    t[i][j]=t[i][j-2]
                    if s[i-1]==p[j-2] or p[j-2]=='.':
                        t[i][j]=t[i-1][j] or t[i][j]
                    # else:
                        
                else:
                    t[i][j]=False
        return t[len(s)][len(p)]
                
        
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        
