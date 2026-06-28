import itertools
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        c=list(permutations(nums))
        return list(map(list,c))
    
