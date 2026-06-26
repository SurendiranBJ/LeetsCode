class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        intervals.sort()
        ans=[]
        last=float('-inf')
        for i in intervals:
            if last<i[0]:
                last=i[1]
                ans.append([i[0],i[1]])
            else:
                j=ans[-1]
                ans.pop(-1)
                ans.append([min(i[0],j[0]),max(i[1],j[1])])
                last=max(i[1],j[1])
        return ans            