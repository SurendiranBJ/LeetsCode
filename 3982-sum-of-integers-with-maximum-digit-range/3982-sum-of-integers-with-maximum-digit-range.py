class Solution:
    def maxDigitRange(self, nums: list[int]) -> int:
        di={}
        for i in nums:
            sol=list(str(i))
            d=int(max(sol))-int(min(sol))
            if d not in di:
                di[d]=0
                di[d]+=i
            else:
                di[d]+=i
        di=sorted(di.items(),reverse=True)  
        return di[0][1]