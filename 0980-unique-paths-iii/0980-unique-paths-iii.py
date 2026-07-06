class Solution(object):
    c=0
    tot=0
    def findsol(self,x,y,grid,sol,n,m,count):
        global c,tot
        if x<0 or y<0 or x>m-1 or y>n-1 :
            return False
        if sol[x][y]==1 or grid[x][y]==-1:
            return False  
         
        if grid[x][y]==2 and count==self.tot-1:
            
            self.c+=1
            return False
        sol[x][y]=1
        if self.findsol(x+1,y,grid,sol,n,m,count+1):
            return True            
        if self.findsol(x-1,y,grid,sol,n,m,count+1):
            return True            
        if self.findsol(x,y+1,grid,sol,n,m,count+1):
            return True            
        if self.findsol(x,y-1,grid,sol,n,m,count+1):
            return True   
        sol[x][y]=0
        return False             
    def uniquePathsIII(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        global c,tot
        c=0
        m=len(grid)
        n=len(grid[0])
        a,b=0,0
        ob=0
        tot=0
        sol=[[0]*n for i in range(m)]
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1:
                    a=i
                    b=j
                if grid[i][j]==-1:
                    ob+=1
        print(a,b)               
        self.tot=(n*m)-ob
        self.findsol(a,b,grid,sol,n,m,0)
        return self.c