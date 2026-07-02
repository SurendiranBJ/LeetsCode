
class Solution:
    n=0
    m=0
    key=False
    sol=[]
    al=[]
    def findsol(self,x,y,health,grid):
        global sol,n,m,key,al
        if x<0 or y<0 or x>n-1 or y>m-1 or sol[x][y]==1 or health-grid[x][y]<1:
            return False     
        if x==n-1 and y==m-1 and health-grid[x][y]>=1:
            self.key=True
            return True
        if health-grid[x][y]<1:
            return False   
        if health<=al[x][y]:
            return False
        else:
            al[x][y]=health    
        sol[x][y]=1
        if self.findsol(x+1,y,health-grid[x][y],grid):
            return True
        if self.findsol(x-1,y,health-grid[x][y],grid):
            return True   
        if self.findsol(x,y+1,health-grid[x][y],grid):
            return True
        if self.findsol(x,y-1,health-grid[x][y],grid):
            return True
        sol[x][y]=0  
        return False    


    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
        global n,m,sol,key,al
        n=len(grid)
        m=len(grid[0])
        al=[[-1]*m for i in range(n)]
        sol=[[0]*m for i in range(n)]
        self.findsol(0,0,health,grid)
        if self.key:
            return True
        else:
            return False    