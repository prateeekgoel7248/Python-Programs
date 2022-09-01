class Solution:
    # @param A : list of list of integers
    # @return an integer
    def solve(self, A):
        from collections import defaultdict
        di=defaultdict(lambda :0)
        a=[i[0] for i in A]
        b=[i[1] for i in A]
        di = dict(zip(a,b))
        for i in A:
            if di[i[0]]:
                di[i[0]]=max(di[i[0]],i[1])
            else:
                di[i[0]]=i[1]
        # print(di)
        s=0
        for i,j in di.items():
            if i!=0:
                s+=i
                di.pop(i)
                if di[i//2]==0:
                    di[i//2]=max(di[i//2],i*2)
                else:
                    di[i//2]=i*2

        return s