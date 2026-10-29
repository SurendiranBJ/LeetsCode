class Solution:
    board=[]
    for i in range(8):
        r=[]
        if i%2==0:
            for j in range(8+1):
                if j%2==0:
                    r.append(1)
                else:
                    r.append(0)
                    
        else:
            for j in range(8+1):
                if j%2==0:
                    r.append(0)
                else:
                    r.append(1)
        board.append(r)

    def squareIsWhite(self, coordinates: str) -> bool:
        di={'a':0,'b':1,'c':2,'d':3,'e':4,'f':5,'g':6,'h':7}
        r=di[coordinates[0]]
        c=int(coordinates[1])
        if self.board[r][c]:
            return True
        else:
            return False
