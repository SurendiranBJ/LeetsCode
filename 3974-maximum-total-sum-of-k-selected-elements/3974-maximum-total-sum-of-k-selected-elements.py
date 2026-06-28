class Solution(object):
    def maxSum(self, nums, k, mul):
        """
        :type nums: List[int]
        :type k: int
        :type mul: int
        :rtype: int
        """
        ans=0
        nums.sort(reverse=True)
        c=0
        while c<k:
            if mul>0:
                ans+=nums[c]*mul
                mul-=1
                c+=1
            else:
                ans+=nums[c]
                c+=1
        return ans        