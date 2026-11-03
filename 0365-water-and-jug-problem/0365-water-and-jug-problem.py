from collections import deque
class Solution:
    def canMeasureWater(self, X: int, Y: int, target: int) -> bool:
        visi=set()
        q=deque()
        q.append((0,0))
        while q:
            x,y=q.popleft()
            if x+y==target:
                return True
            li=[]
            li.append((X,y))
            li.append((x,Y))
            li.append((0,y))
            li.append((x,0))
            z=min(X-x,y)
            if z<=y:
                li.append((x+z,y-z))
            z=min(Y-y,x)
            if z<=x:
                li.append((x-z,y+z))
            for i,j in li:
                if (i,j) not in visi:
                    q.append((i,j))
                    visi.add((i,j))
        return False
            