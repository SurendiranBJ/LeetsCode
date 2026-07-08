class Solution(object):
    def getMinDistance(self, nums, target, start):
        """
        :type nums: List[int]
        :type target: int
        :type start: int
        :rtype: int
        """
        ans=float('inf')
        for i,j in enumerate(nums):
            if j==target:
                if ans>abs(i-start):
                    ans=abs(i-start)
        return ans         