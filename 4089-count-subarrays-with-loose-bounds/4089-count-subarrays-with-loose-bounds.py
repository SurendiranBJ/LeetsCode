class Solution:
    def countSubarrays(self, nums: list[int], minK: int, maxK: int) -> int:
        ans=0
        sol=0
        for i in range(len(nums)):
            if nums[i]>=minK and nums[i]<=maxK:
                sol+=1
            else:
                ans+=((sol*(sol+1))//2)
                sol=0
        if sol!=0:
            ans+=((sol*(sol+1))//2)
        return ans