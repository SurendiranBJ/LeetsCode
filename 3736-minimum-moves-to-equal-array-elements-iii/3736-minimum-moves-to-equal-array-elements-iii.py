class Solution:
    def minMoves(self, nums: List[int]) -> int:
        maxi=max(nums)
        ans=0
        for i in nums:
            if i!=maxi:
                ans+=(maxi-i)
        return ans