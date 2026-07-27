import itertools
class Solution(object):
    def maxProduct(self, n):
        """
        :type n: int
        :rtype: int
        """
        ans=float('-inf')
        nums=list(str(n))
        nums=map(int,nums)
        sol=list(itertools.combinations(nums,2))
        for i,j in sol:
            ans=max(ans,i*j)
        return ans    