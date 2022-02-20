#User function Template for python3

class Solution:

    def longestKSubstr(self, s, k):
        i=0
        j=0
        d=dict()
        mx=-1
        while j<len(s):
            if s[j] in d:
                d[s[j]]+=1
            else:
                d[s[j]]=1
            if len(d)<k:
                j+=1
            elif len(d)==k:
                mx=max(mx,j-i+1)
                j+=1
            elif len(d)>k:
                while len(d)>k:
                    if d[s[i]]==1:
                        d.pop(s[i])
                    else:
                        d[s[i]]-=1
                    i+=1
                j+=1
            
                
            # j+=1
        return mx
        # code here

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        s = input()
        k = int(input())

        solObj = Solution()

        ans = solObj.longestKSubstr(s, k)

        print(ans)

# } Driver Code Ends
