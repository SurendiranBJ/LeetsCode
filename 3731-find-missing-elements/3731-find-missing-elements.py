class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        maxi=max(nums)
        mini=min(nums)
        sol=[i for i in range(mini,maxi+1)]
        sol=set(sol)^set(nums)
        return sorted(list(sol))