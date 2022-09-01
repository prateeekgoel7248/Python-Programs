from copy import deepcopy
from collections import deque
def f(n,res):
    q = deque()
    for i in range(n):
        if ind2[i]==1:
            q.append(i)
    while q:
        t = q.popleft()
        exp[t]=1
        for j in adj[t]:
            if not exp[j-1]:
                res+=ind2[j-1]
        for i in adj[t]:
            ind2[i-1]-=1
            if ind2[i-1]==1:
                q.append(i-1)
    return res
T = int(input())
for t in range(T):
    n,q = map(int,input().split())
    adj=[[] for i in range(n)]
    ind=[0]*(n)
    exp=[0]*(n)
    for i in range(n-1):
        u,v = map(int,input().split())
        adj[u-1].append(v)
        adj[v-1].append(u)
        ind[u-1]+=1
        ind[v-1]+=1
    res = 0
    ind2=ind.copy()
    res = f(n,res)
    print(res)
    for i in range(q):
        a,b,c,d=map(int,input().split())
        res2=deepcopy(res)
        res2-=ind[a-1]+ind[b-1]
        if a==c or b==c:
            res2+=ind[c-1]
        else:
            res2+=ind[c-1]+1
        if a==d or b==d:
            res2+=ind[d-1]
        else:
            res2+=ind[d-1]+1
        print(res2)