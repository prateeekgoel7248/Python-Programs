class Solution(object):
    def findOrder(self, n, edges):
        #using topo sort
        indegree=[0 for _ in range(n)]
        adj=defaultdict(list)
        for i,j in edges:
            adj[j].append(i)
            indegree[i]+=1
        q=[]
        for i in range(n):
            if indegree[i]==0:
                q.append(i)
        ans=[]
        while q:
            ans.append(q[0])
            node = q.pop(0)
            for nei in adj[node]:
                indegree[nei]-=1
                if indegree[nei]==0:
                    q.append(nei)
        if sum(indegree)>0:
            return []
        return ans
        
        