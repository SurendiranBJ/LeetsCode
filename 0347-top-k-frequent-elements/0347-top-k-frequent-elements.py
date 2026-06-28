from collections import Counter
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        di={}
        ans=[]
        s=set(nums)
        for i in s:
            di[i]=nums.count(i)
        print(max(di))    
        for i in range(k):
            ma=max(di,key=di.get)
            ans.append(ma)
            del di[ma]
        return ans

        