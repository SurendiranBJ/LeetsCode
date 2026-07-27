class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans=[]
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i!=j:
                    sol=(nums[i]-1)*(nums[j]-1)
                    ans.append(sol)
                   
        return max(ans)           