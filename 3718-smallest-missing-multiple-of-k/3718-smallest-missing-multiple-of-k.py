class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        for i in range(1,101):
            if i*k not in nums:
                return i*k
        return max(nums)+1        