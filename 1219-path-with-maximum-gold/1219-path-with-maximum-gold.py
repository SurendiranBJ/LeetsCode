class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        ans=0
        def findsol(x,y,grid,sol,s):
            nonlocal ans
            if x<0 or y<0 or x>=n or y>=m or sol[x][y]==1 or grid[x][y]==0:
                return
            s+=grid[x][y]
            sol[x][y]=1
            findsol(x+1,y,grid,sol,s)
            findsol(x,y+1,grid,sol,s)
            findsol(x,y-1,grid,sol,s)    
            findsol(x-1,y,grid,sol,s)
            sol[x][y]=0
            ans=max(ans,s)
            return
        n=len(grid)
        m=len(grid[0])
        sol=[[0]*m for i in range(n)]
        for i in range(n):
            for j in range(m):
                if grid[i][j]>0:
                    findsol(i,j,grid,sol,0)
        return ans          
