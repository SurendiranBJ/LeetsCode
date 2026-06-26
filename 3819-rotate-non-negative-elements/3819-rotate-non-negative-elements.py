from collections import deque
class Solution(object):
    def rotateElements(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        li=[]
        for i,j in enumerate(nums):
            if j<0:
                li.append((i,j))
        nn=[]
        for i in nums:
            if i>=0:
                nn.append(i)     
        nn=deque(nn)
        nn.rotate(-k)
        print(nn)
        nn=list(nn)
        for i,j in li:
            nn.insert(i,j)
        return nn    
          