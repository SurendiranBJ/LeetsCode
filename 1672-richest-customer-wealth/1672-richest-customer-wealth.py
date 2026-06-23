class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        ans=[]
        for i in accounts:
            ans.append(sum(i))
        return max(ans)    
        