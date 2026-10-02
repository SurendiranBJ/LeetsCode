class Solution:
    def validPath(self, n: int, edges: list[list[int]], source: int, destination: int) -> bool:
        grid=[[] for i in range(n)]
        for i,j in edges:
            grid[i].append(j)
            grid[j].append(i)
        key=False    
        def dfs(cur):
            nonlocal key
            visi.add(cur)
            if cur==destination:
                key=True
                return
            for nei in grid[cur]:
                if nei not in visi:
                    dfs(nei)         
        visi=set()
        dfs(source)
        if key:
            return True
        else:
            return False    
