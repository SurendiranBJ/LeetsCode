from collections import deque
import copy
class Solution:
    def minimumOperationsToMakeEqual(self, x: int, y: int) -> int:
        visi=set()
        q=deque()
        visi.add(x)
        q.append((x,0))
        while q:
            cur,cost=q.popleft()
            if cur==y:
                return cost
            st=[]
            if cur%11==0:
                st.append((cur/11))
            if cur%5==0:
                st.append(cur/5)
            st.append(cur-1)    
            st.append(cur+1)
            for i in st:
                if i not in visi:
                    q.append((i,cost+1))
                    visi.add(i)


               