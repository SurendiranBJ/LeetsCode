class Solution:
    def mergeTriplets(self, triplets: list[list[int]], target: list[int]) -> bool:
        ans=[0,0,0]
        for i,j,k in triplets:
            if i<=target[0] and j<=target[1] and k<=target[2]:
                ans[0]=max(ans[0],i)
                ans[1]=max(ans[1],j)
                ans[2]=max(ans[2],k)
        if ans==target:
            return True
        else:
            return False
