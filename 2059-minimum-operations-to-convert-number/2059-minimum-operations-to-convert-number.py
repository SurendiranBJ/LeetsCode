from collections import deque
class Solution:
    def minimumOperations(self, nums: list[int], start: int, goal: int) -> int:
        q=deque()
        visi=set()
        q.append((start,0))
        visi.add(start)
        while q:
            cur,cost=q.popleft()
            for i in nums:
                add=cur+i
                sub=cur-i
                xor=cur^i
                if add==goal:
                    return cost+1
                if sub==goal:
                    return cost+1
                if xor==goal:
                    return cost+1    
                if 0<=add<=1000 and add not in visi:
                    q.append((add,cost+1))
                    visi.add(add)
                if 0<=sub<=1000 and sub not in visi:
                    q.append((sub,cost+1))
                    visi.add(sub)
                if 0<=xor<=1000 and xor not in visi:
                    q.append((xor,cost+1))
                    visi.add(xor)
        return -1            
