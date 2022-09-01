class Solution:
    # @param A : list of integers
    # @param B : integer
    # @param C : integer
    # @return a list of list of integers
    def solve(self, A, B, C):
        row=B
        # if row==0:
        #     return lis
        col=C
        lis=[[0 for _ in range(C)] for m in range(B)]
        if B*C!=len(A):
            return -1
        
        # lis=[]
        l=0
        r=col-1
        t=0
        b=row-1
        d=0
        k=0
        while k<len(A):
            if d==0:
                for i in range(l,r+1):
                    lis[t][i]=A[k]
                    k+=1
                t+=1
                # d=
                d=1
            elif d==1:
                for i in range(t,b+1):
                    lis[i][r]=A[k]
                    k+=1
                r-=1
                d=2
            elif d==2:
                for i in range(r,l-1,-1):
                    lis[b][i]=A[k]
                    k+=1
                b-=1  
                d=3
            elif d==3:
                for i in range(b,t-1,-1):
                    lis[i][l]=A[k]
                    k+=1
                d=0
                l+=1
            # k+=1
        return lis