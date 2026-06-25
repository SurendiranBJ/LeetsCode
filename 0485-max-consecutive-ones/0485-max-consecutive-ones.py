class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans=0
        c=0
        left=0
        if len(nums)==1:
            return nums[0]  
        for right in range(len(nums)):
            if nums[right]==1:
                c+=1
            while nums[right]!=1:
                if nums[left]==1:
                    c-=1
                left+=1
                if left==right or left>right:
                    break
            ans=max(ans,c)
        return ans                    