class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
        if len(A)>=8 and len(A)<=15:
            n=0
            lower=0
            upper=0
            special=0
            for i in A:
                if i.isnumeric():
                    n+=1
                if i=="@" or i=="#" or i=="%" or i=="&" or i=="!" or i=="$" or i=="*":
                    special+=1
                if i.isupper():
                    upper+=1
                if i.islower():
                    lower+=1
            if n>0 and lower>0 and upper>0 and special>0:
                return 1
            else:
                return 0
        else:
            return 0