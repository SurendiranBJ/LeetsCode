class Solution(object):
    def longestOnes(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        ans=0
        left=0
        zero=0
        for right in range(len(nums)):
            if nums[right]==0:
                zero+=1
            while zero>k:
                if nums[left]==0:
                    zero-=1
                left+=1
            if zero<=k:
                ans=max(ans,right-left+1)
                
        return ans            