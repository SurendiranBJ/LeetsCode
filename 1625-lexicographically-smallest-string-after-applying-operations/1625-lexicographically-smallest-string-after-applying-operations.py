from collections import deque
import heapq
class Solution:
    def findLexSmallestString(self, s: str, a: int, b: int) -> str:
        q=deque()
        visi=set()
        q.append(s)
        visi.add(s)
        l=len(s)
        while q:
            cur=deque(list(q.popleft()))
            r=cur
            r.rotate(b)
            r=''.join(r)
            if r not in visi:
                visi.add(r)
                q.append(r)
            for j in range(1,l,2):
                cur[j]=str((int(cur[j])+a)%10)
            cur=''.join(cur)
            if cur not in visi:
                q.append(cur)
                visi.add(''.join(cur))
        return min(list(visi))     