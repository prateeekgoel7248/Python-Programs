class Solution(object):
    def smallestStringWithSwaps(self, s, pairs):
        s=[i for i in s]
        adj=[[] for i in range(100001)]
        visited=[False for i in range(100001)]
        def DFS(s,vertex,characters,indices):
            characters.append(s[vertex])
            indices.append(vertex)
            visited[vertex]=True
            for adjacent in adj[vertex]:
                if not visited[adjacent]:
                    DFS(s,adjacent,characters,indices)
        for edge in pairs:
            source=edge[0]
            destination=edge[1]
            
            adj[source].append(destination)
            adj[destination].append(source)
        for vertex in range(len(s)):
            characters=[]
            indices=[]
            if not visited[vertex]:
                DFS(s,vertex,characters,indices)
                characters.sort()
                indices.sort()
                for index in range(len(characters)):
                    s[indices[index]]=characters[index]
        return ''.join(s)
                    
        