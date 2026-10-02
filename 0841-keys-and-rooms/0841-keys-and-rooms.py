from collections import deque
class Solution:
    def canVisitAllRooms(self, rooms: list[list[int]]) -> bool:
        keys=set()
        q=deque()
        q.append((0))
        keys.add(0)
        while q:
            cur=q.popleft()
            for nei in rooms[cur]:
                if nei not in keys:
                    q.append(nei)
                    keys.add(nei)
        print(keys)            
        if len(keys)==len(rooms):
            return True
        else:
            return False             