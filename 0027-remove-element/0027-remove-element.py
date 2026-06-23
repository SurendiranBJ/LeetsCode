class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        c=0
        while nums.count(val)>0:
            for i in range(len(nums)):
                if nums[i]==val:
                    t=nums[i]
                    for j in range(i,len(nums)-1):
                        nums[j]=nums[j+1]
                    nums[len(nums)-1]='#'
                    c+=1
        return len(nums)-c                