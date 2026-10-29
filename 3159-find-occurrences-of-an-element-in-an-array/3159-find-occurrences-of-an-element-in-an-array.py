class Solution:
    def occurrencesOfElement(self, nums: List[int], queries: List[int], x: int) -> List[int]:
        sol=[]
        ans=[]
        for i in range(len(nums)):
            if nums[i]==x:
                sol.append(i)
        for q in queries:
            if (q-1)>=len(sol):
                ans.append(-1)
            else:
                ans.append(sol[q-1])
        return ans