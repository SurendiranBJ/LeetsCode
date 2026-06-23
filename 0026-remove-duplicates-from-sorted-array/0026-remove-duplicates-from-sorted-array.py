class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i=0
        j=0
        while j<=len(nums)-1:
            if nums[j]!=nums[i]:
                i+=1
                nums[i]=nums[j]
            else:
                j+=1
        return i+1            
        