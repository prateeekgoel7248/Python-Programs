class Solution(object):
    def spiralOrder(self, matrix):
        row=len(matrix)
        if row==0:
            return lis
        col=len(matrix[0])
        lis=[]
        # if B*C!=len(A):
        #     return -1
        
        lis=[]
        l=0
        r=col-1
        t=0
        b=row-1
        d=0
        while l<=r and t<=b:
            if d==0:
                for i in range(l,r+1):
                    lis.append(matrix[t][i])
                t+=1
                # d=
                d=1
            elif d==1:
                for i in range(t,b+1):
                    lis.append(matrix[i][r])
                r-=1
                d=2
            elif d==2:
                for i in range(r,l-1,-1):
                    lis.append(matrix[b][i])
                b-=1  
                d=3
            elif d==3:
                for i in range(b,t-1,-1):
                    lis.append(matrix[i][l])
                d=0
                l+=1
        return lis
        