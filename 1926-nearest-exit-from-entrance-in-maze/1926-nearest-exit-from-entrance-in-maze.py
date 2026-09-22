from collections import deque
class Solution:
    def nearestExit(self, maze: list[list[str]], entrance: list[int]) -> int:
        n,m=len(maze),len(maze[0])
        q=deque()
        q.append((entrance[0],entrance[1],0))
        visi=set()
        visi.add((entrance[0],entrance[1]))
        dir=[[0,1],[0,-1],[1,0],[-1,0]]
        while q:
            x,y,cost=q.popleft()
            if (x==0 or x==n-1 or y==0 or y==m-1) and [x,y]!=entrance:
                return cost
            for i,j in dir:
                nr,nc=x+i,y+j
                if nr>=n or nc>=m or nr<0 or nc<0:
                    continue
                if (nr,nc) in visi:
                    continue    
                if maze[nr][nc]=='+':
                    continue
                q.append((nr,nc,cost+1))
                visi.add((nr,nc))
        return -1            