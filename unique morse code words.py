class Solution(object):
    def uniqueMorseRepresentations(self, words):
        lst=[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        res=set()
        for i in words:
            ans=""
            for j in i:
                ans+=lst[ord(j)-97]
            res.add(ans)
            # print(ans)
        return len(res)
        