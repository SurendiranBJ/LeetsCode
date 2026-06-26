from collections import Counter
class Solution(object):
    def maximumSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if len(nums)<k:
            return 0
        ans=0
        di={}
        c=0
        for i in range(k):
            di[nums[i]]=di.get(nums[i],0)+1
            c+=nums[i]
        if len(di)==k:
            ans=c
        for i in range(k,len(nums)):
            di[nums[i-k]]-=1
            c-=nums[i-k]
            if di[nums[i-k]]==0:
                del di[nums[i-k]] 
            di[nums[i]]=di.get(nums[i],0)+1
            c+=nums[i]
            if len(di)==k:
                ans=max(ans,c)
        return ans    