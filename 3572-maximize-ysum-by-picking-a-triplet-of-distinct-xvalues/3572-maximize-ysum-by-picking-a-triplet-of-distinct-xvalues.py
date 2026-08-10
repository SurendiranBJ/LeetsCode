class Solution:
    def maxSumDistinctTriplet(self, x: List[int], y: List[int]) -> int:
        di={}
        for i in range(len(y)):
            if y[i] not in di:
                di[y[i]]=[]
                di[y[i]].append(i)
            else:
                di[y[i]].append(i)    
        y1=sorted(list(set(y)),reverse=True) 
        ans=0
        sol=set()
        for i in y1:
            for j in di[i]:
                if x[j] not in sol:
                    ans+=y[j]
                    sol.add(x[j])
                if len(sol)==3:
                    return ans
        return -1                