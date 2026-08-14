class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def findsol(x,y,sol,l,idx):
            global key
            if x<0 or y<0 or x>=n or y>=m or sol[x][y]==1 or board[x][y]!=word[idx]:
                return False
            if len(word)==l:
                key=True
                return True
            sol[x][y]=1
            if findsol(x+1,y,sol,l+1,idx+1):
                return True
            if findsol(x-1,y,sol,l+1,idx+1):
                return True
            if findsol(x,y+1,sol,l+1,idx+1):
                return True
            if findsol(x,y-1,sol,l+1,idx+1):
                return True
            sol[x][y]=0
            return False    




        key=False
        ans=[]
        n=len(board)
        m=len(board[0])
        sol=[[0]*m for i in range(n)]
        for i in range(n):
            for j in range(m):
                if board[i][j]==word[0]:
                    if findsol(i,j,sol,1,0):
                        return True
                        
        return False                        
