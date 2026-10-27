from collections import deque
class Solution:
    def minLengthAfterRemovals(self, s: str) -> int:
        a,b=0,0
        for i in s:
            if i=='a':
                a+=1
            elif i=='b':
                b+=1
        return abs(a-b)