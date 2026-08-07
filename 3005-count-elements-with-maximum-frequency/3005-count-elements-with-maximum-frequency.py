from collections import Counter
class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        di=Counter(nums)
        li=sorted(di.items(),key=lambda x:x[1],reverse=True)
        sol=[count for i,count in li]
        sol1=Counter(sol)  
        return sol[0]*sol1[sol[0]]

