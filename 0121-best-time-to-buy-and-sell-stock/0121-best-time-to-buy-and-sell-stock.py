class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        maxi=0
        mini=99999999
        p=0
        for i in range(len(prices)):
            if prices[i]<mini:
                mini=prices[i]
            else:
                p=prices[i]-mini
            maxi=max(p,maxi)
        return maxi                  