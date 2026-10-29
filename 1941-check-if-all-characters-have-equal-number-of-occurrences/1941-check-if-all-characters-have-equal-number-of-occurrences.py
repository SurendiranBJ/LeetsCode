from collections import Counter
class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        c=Counter(s)
        k=0
        if len(c)==1:
            return True
        for i,j in c.items():
            if k:
                if pre!=j:
                    return False
            else:
                k=1
                pre=j
        return True