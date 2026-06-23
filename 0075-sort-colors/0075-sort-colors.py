class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums)):
            mini=i
            for j in range(i+1,len(nums)):
                if nums[mini]>nums[j]:
                    
                    mini=j
            nums[mini],nums[i]=nums[i],nums[mini]               