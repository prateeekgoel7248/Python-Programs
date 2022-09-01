class Solution:
    def countVowels(self, word: str) -> int:
        vowel=['a','e','i','o','u']
        n=len(word)
        cnt = 0
        for i in range(len(word)):
            if word[i] in vowel:
                cnt+=(i+1)*(n-i)
        return cnt
    #lets take an example to get the clarity for that math
    #  "xyzabc"
    # so how many combination we can make for this string
    # there is only one "a" and we have to find the combinations
    # so 
    # xyza,xyzab,xyzabc,yza,yzab,yzabc,za,zab,zabc,a,ab,abc
    # so 3 in the left of a and 2 will be on the right of a
    # so (3+1)*(2+1)=4*3=12 so we got 12 combination
    
    
    
    
    '''
    xyza + b or c = +2
    yza  + b or c = +2
    za   + b or c = +2
    a    + b or c = +2
    
    so 4 +(4*2)= 4+8=12
    
    '''
        