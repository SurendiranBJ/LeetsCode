class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        absum=sum(nums)
        ans=0
        l=nums[0]
        for i in range(1,len(nums)):
            c=l-absum
            if (l-c)%2==0:
                ans+=1
            l+=nums[i]
        return ans