class Solution(object):
    def separateDigits(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans=[]
        for i in nums:
            if len(str(i))==1:
                ans.append(int(i))
            else:
                for j in str(i):
                    ans.append(int(j))
        return ans