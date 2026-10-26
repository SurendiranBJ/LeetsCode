from collections import deque
class Solution:
    def closedIsland(self, grid: list[list[int]]) -> int:
        def bfs(x,y):
            nonlocal q,visi,ans
            q.append((x,y))
            visi.add((x,y))
            key=True
            while q:
                cr,cc=q.popleft()
                for i,j in [[1,0],[0,1],[-1,0],[0,-1]]:
                    nr,nc=cr+i,cc+j
                    if nr<0 or nc<0 or nr>=r or nc>=c:
                        continue
                    if (nr,nc) in visi:
                        continue
                    if grid[nr][nc]==1:
                        continue
                    if nr == 0 or nr == r - 1 or nc == 0 or nc == c - 1 and grid[nr][nc]==0:
                        key=False
                    q.append((nr,nc))
                    visi.add((nr,nc))
            if key:
                ans+=1
        r=len(grid)
        c=len(grid[0])
        visi=set()
        q=deque()
        ans=0
        for i in range(r):
            for j in range(c):
                if not (i == 0 or i == r - 1 or j == 0 or j == c - 1) and (i,j) not in visi and grid[i][j]!=1:
                    q=deque()
                    bfs(i,j)
                
        return ans