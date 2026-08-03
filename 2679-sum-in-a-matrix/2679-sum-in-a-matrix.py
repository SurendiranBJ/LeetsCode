class Solution:
    def matrixSum(self, nums: List[List[int]]) -> int:
        ans=0
        while len(nums[0])>0:
            sol=[]
            for i in range(len(nums)):
                v=(max(nums[i]))
                nums[i].remove(v)
                sol.append(v)    
            ans+=max(sol)
        return ans  