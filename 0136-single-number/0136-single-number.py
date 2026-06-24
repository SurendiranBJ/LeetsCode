class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans=0
        for i in nums:
            if nums.count(i)==1:
                return i