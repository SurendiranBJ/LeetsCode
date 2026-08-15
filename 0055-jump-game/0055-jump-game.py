class Solution:
    def canJump(self, nums: List[int]) -> bool:
        l=len(nums)
        dp=[False]*(len(nums)+1)
        if nums[0]==0 and len(nums)==1:
            return True
        if nums[0]==0:
            return False
        if l==1:
            return True
        dp[0]=True    
        m=-1
        for i in range(0,l-1):
            if dp[l]==True:
                return True  
            if nums[i]==0 and m==i:
                return False
            if i+nums[i]>m:
                for j in range(i+1,i+nums[i]+1):
                    if j<l:
                        dp[j]=True
                        m=j
                    else:
                        break    
        return dp[l-1]                

                