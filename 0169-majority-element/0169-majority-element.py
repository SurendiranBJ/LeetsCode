class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        se=set(nums)
        n=len(nums)/2
        for i in se:
            if nums.count(i)>=n:
                return i
        
                