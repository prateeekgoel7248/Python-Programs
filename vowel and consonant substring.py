class Solution:
    # @param A : string
    # @return an integer
    def solve(self,A):
        vow = 0
        con = 0
        for i in range(0, len(A)):
            if A[i] in ["a", "e", "i", "o", "u"]:
                vow = vow + 1
            else:
                con = con + 1
        count = (vow * con) % 1000000007
        return count