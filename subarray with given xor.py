class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        count=0
        xor=0
        from collections import defaultdict
        d=defaultdict(int)
        for i in A:
            xor^=i
            if xor==B:
                count+=1
            if d[xor^B]>0:
                #it is working like when we are at any position in the array and we got A
                # value of xor and we try to get that is there any previous xor with the xor value of xor^B value if yes then we will add there value into the ans
                #lets take the example  A = [4, 2, 2, 6, 4] , B = 6
                #here when 
                #1) first iteration we have have 4 the xor value = 4 and we try to get a value of 4^6 =2 in the array if there exist an element with the value of xor 2 then we will add their value into the ans
                
                #
                #
                #
                #
                #
                #
                #
                #
                #
                #
                count+=d[xor^B]
            d[xor]+=1
        return count
            