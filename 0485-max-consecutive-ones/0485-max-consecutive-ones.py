class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        c=0
        arr=[]
        for i in nums:
            if i==1:
                c+=1
            elif i==0:
                arr.append(c)
                c=0     
        arr.append(c)
        return max(arr)