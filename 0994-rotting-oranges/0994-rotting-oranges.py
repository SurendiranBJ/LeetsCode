from collections import deque
class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        fresh=0
        rotten=0
        q=deque()
        visi=set()
        r=len(grid)
        c=len(grid[0])
        for i in  range(r):
            for j in range(c):
                if grid[i][j]==1:
                    fresh+=1
                elif grid[i][j]==2:
                    rotten+=1
                    q.append((i,j))
        ans=0
        if rotten==0 and fresh==0:
            return 0 
        if rotten==0:
            return -1
        if fresh==0:
            return 0
        while q:
            l=len(q)
            for k in range(l):
                cr,cc=q.popleft()
                for i,j in [[0,1],[0,-1],[1,0],[-1,0]]:
                    nr,nc=i+cr,j+cc
                    if (nr,nc) in visi:
                        continue
                    if nr<0 or nr>=r or nc<0 or nc>=c:
                        continue
                    if grid[nr][nc]==0:
                        continue
                    if grid[nr][nc]==2:
                        continue
                    visi.add((nr,nc))
                    fresh-=1
                    q.append((nr,nc))
            ans+=1
        if fresh==0:
            return ans-1
        else:
            return -1