class Solution(object):
    def wordBreak(self, s, wordDict):
        lst  = []
        def rec(start,sentence):
            if start >= len(s):
                lst.append(sentence[:-1]) #[:-1] bcz at last of the sentence there is space to not incluide it I use last index

            for i in range(start,len(s)):      # evert time I am going in forwad directon if the below IF condition satisfy
                if s[start:i+1] in wordDict:
                    rec(i+1,sentence + s[start:i+1] + " ")  # In question they have mension that give space between each word
                    
        rec(0,'')
        return lst

#just an easy implementation, try to look at code after breathing and  you will understand all the things very easily.