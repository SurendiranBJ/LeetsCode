from collections import Counter
class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        c=Counter(arr)
        sol = [list(item) for item in sorted(c.items(), key=lambda item: item[1], reverse=False)]
        idx=0
        for i in  range(k):
            sol[idx][1]-=1
            if sol[idx][1]==0:
                idx+=1
        return len(sol)-idx
        