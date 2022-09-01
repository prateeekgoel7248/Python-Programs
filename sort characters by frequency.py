class Solution:
    def frequencySort(self, s: str) -> str:
        res=[]
        for i in set(s):
            res.append([i,s.count(i)])
        res = sorted(res,key=lambda x:-x[1])
        # print(res)
        ans=""
        for i,j in res:
            ans+=(i*j)
        return ans
            
        
            
        