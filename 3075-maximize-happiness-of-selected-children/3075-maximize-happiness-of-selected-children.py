class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        ans=0
        happiness.sort()
        j=0
        for i in range(len(happiness)-1,-1,-1):
            if j!=k:
                if happiness[i]-j>0:
                    ans+=(happiness[i]-j)
                    j+=1
                elif j!=k and (happiness[i]<=0 or happiness[i]-j<=0):
                    ans+=0
                    j+=1   
            else:
                break
        return ans
                