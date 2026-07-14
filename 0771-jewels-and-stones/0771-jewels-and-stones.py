from collections import Counter
class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        """
        :type jewels: str
        :type stones: str
        :rtype: int
        """
        di=Counter(stones)
        ans=0
        for i in jewels:
            ans+=di[i]
        return ans    