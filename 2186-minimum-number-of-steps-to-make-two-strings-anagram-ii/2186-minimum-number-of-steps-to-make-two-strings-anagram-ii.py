class Solution:
    def minSteps(self, s: str, t: str) -> int:
        ds={}
        for i in s:
            ds[i]=ds.get(i,0)+1
        dt={}
        for i in t:
            dt[i]=dt.get(i,0)+1
        ans=0
        for i in s:
            if i not in dt:
                ans+=1
            else:
                if dt[i]==0:
                    ans+=1
                else:
                    dt[i]-=1
        for i in t:
            if i not in ds:
                ans+=1
            else:
                if ds[i]==0:
                    ans+=1
                else:
                    ds[i]-=1
        return ans