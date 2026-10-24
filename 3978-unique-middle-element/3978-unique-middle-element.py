from collections import Counter
class Solution:
    def isMiddleElementUnique(self, nums: list[int]) -> bool:
        c=Counter(nums)
        mid=len(nums)//2
        if c[nums[mid]]==1:
            return True
        else:
            return False