from collections import Counter
class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        di=Counter(stones)
        j=Counter(jewels)
        ans=0
        for i,j in j.items():
            ans+=di[i]
        return ans    