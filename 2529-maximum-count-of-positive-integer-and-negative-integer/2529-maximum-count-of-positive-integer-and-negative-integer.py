class Solution(object):
    def maximumCount(self, nums):
        c=0
        e=0
        for i in nums:
            if i<0:
                c+=1
            elif i>=1:
                e+=1    
        return max(c,e)    
        """
        :type nums: List[int]
        :rtype: int
        """
        