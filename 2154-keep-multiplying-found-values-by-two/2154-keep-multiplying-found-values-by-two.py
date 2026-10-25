class Solution:
    def findFinalValue(self, nums: list[int], original: int) -> int:
        s=set(nums)
        while original in nums:
            original*=2
        return original