class Solution(object):
    def arrayRankTransform(self, arr):
        li=arr
        s=set(li)
        ans=[]
        sol=sorted(s)
        di={}
        for i in range(len(sol)):
            di[sol[i]]=i+1
        for j in arr:
            ans.append(di[j])    
        return ans