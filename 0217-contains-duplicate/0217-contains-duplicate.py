class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n=len(nums)
        se=set(nums)
        if n-len(se)>=1:
            return True
        else:
            return False    