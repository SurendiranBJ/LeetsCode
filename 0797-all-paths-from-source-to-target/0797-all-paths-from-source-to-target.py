class Solution:
    def allPathsSourceTarget(self, graph: list[list[int]]) -> list[list[int]]:
        
        n=len(graph)
        paths=[]
        def dfs(u,path):
            nonlocal paths
            if u==n-1:
                paths.append(path)
                return
            for v in graph[u]:
                dfs(v,path+[v])
        dfs(0,[0])        
        return paths