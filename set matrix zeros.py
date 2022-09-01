class Solution:
    # @param A : list of list of integers
    # @return the same list modified
    def setZeroes(self, A):
        zerois=set()
        zerojs=set()
        for i in range(len(A)):
            for j in range(len(A[0])):
                if(A[i][j] == 0):
                    zerois.add(i)
                    zerojs.add(j)
        
        for i in zerois:
            for e in range(len(A[0])):
                A[i][e] = 0
        
        for j in zerojs:
            for e in range(len(A)):
                A[e][j] = 0
                
        return A
    # it