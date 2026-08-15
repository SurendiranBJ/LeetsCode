class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        sol=0
        if len(nums)==1 and nums[0]==0:
            return 0
        elif len(nums)==1 and nums[0]!=0:
            return 1
        if nums.count(0)==len(nums):
            return 0    
        for i in nums:
            sol^=i
        if sol==0:
            return len(nums)-1
        else:
            return len(nums)    