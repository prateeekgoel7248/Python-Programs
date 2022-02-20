class Solution:
	# @param A : string
	# @param B : string
	# @return an integer
	def isScramble(self, A, B):
        mem={}
        def solve(A,B):
                
            if len(A)!=len(B):
                return 0
            if A==B:
                return 1
            if len(A)<=1:
                return 0

            if (A,B) in mem:
                return mem[(A,B)]
            flag=0
            for i in range(1,len(A)):
                if((solve(A[0:i],B[len(A)-i:]) and solve(A[i:],B[:len(A)-i])) or (solve(A[:i],B[:i]) and solve(A[i:],B[i:]))):
                    flag = 1
                    mem[(A,B)]=flag
                    break
            mem[(A,B)]=flag
            return flag
        return solve(A,B)
