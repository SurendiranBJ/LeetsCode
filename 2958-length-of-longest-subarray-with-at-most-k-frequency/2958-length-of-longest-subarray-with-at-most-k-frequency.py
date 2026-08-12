class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        s=len(set(nums))
        left=0
        di={}
        ans=0
        for right in range(len(nums)):
            if nums[right] not in di:
                di[nums[right]]=1
            else:
                di[nums[right]]+=1
            while di[nums[right]]>k and left<=right:
                di[nums[left]]-=1        
                left+=1
            if len(di)<=s:
                ans=max(ans,right-left+1)     
        return ans