from collections import deque
class Solution:
    def countIslands(self, grid: List[List[int]], k: int) -> int:
        def bfs(x,y):
            nonlocal q,visi
            sum=0
            sum+=grid[x][y]
            q.append((x,y))
            visi.add((x,y))
            while q:
                cr,cc=q.popleft()
                for i,j in [[1,0],[0,1],[-1,0],[0,-1]]:
                    nr,nc=cr+i,cc+j
                    if nr<0 or nc<0 or nr>=r or nc>=c:
                        continue
                    if (nr,nc) in visi:
                        continue
                    if grid[nr][nc]==0:
                        continue
                    sum+=grid[nr][nc]
                    q.append((nr,nc))
                    visi.add((nr,nc))
            if sum%k==0:
                return True
            else:
                return False
        r=len(grid)
        c=len(grid[0])
        visi=set()
        q=deque()
        ans=0
        for i in range(r):
            for j in range(c):
                if (i,j) not in visi and grid[i][j]!=0:
                    q=deque()
                    if bfs(i,j):
                        ans+=1
        return ans