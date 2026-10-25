from collections import Counter
class Solution:
    def duplicateNumbersXOR(self, nums: List[int]) -> int:
        c=Counter(nums)
        ans=0
        for i,j in c.items():
            if j==2:
                ans^=i
        return ans