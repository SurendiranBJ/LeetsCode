class Solution:
    def addRungs(self, rungs: list[int], dist: int) -> int:
        ans=0
        l=len(rungs)
        if rungs[0]>dist:
            if rungs[0]%dist==0:
                y=rungs[0]-dist
                ans+=(y//dist)
            else:
                y=rungs[0]-dist
                ans+=(y//dist)+1
        for i in range(l-1):
            if rungs[i+1]-rungs[i]<=dist:
                continue
            else:
                y=rungs[i+1]-rungs[i]-1
                ans+=(y//dist)
        return ans