from collections import Counter
class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        di=Counter(stones)
        ans=0
        for i in jewels:
            ans+=di[i]
        return ans    