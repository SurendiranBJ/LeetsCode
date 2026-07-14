from itertools import combinations
class Solution(object):
    def countPairs(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        li=list((combinations(nums,2)))
        ans=0
        for i in li:
            if sum(i)<target:
                print(i)
                ans+=1
        return ans